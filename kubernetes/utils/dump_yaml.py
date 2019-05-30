from yaml import SafeDumper, MappingNode, ScalarNode


class Dumper(SafeDumper):
    def __init__(self, *args, **kwargs):
        if "allow_null_tag" in kwargs:
            self.allow_null_tag = kwargs["allow_null_tag"]
            kwargs.pop("allow_null_tag")
        super(Dumper, self).__init__(*args, **kwargs)

    def represent_mapping(self, tag, mapping, flow_style=None):
        value = []
        node = MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, "items"):
            mapping = list(mapping.items())
            if self.sort_keys:
                try:
                    mapping = sorted(mapping)
                except TypeError:
                    pass
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)

            # transform node_key from snake to camel case
            while "_" in node_key.value:
                i = node_key.value.index("_")
                node_key.value = "{head}{upper}{tail}".format(
                    head=node_key.value[:i + 1],
                    upper=node_key.value[i + 1].upper(),
                    tail=node_key.value[i + 2:],
                )
                node_key.value = node_key.value.replace("_", "", 1)

            node_value = self.represent_data(item_value)
            if (not self.allow_null_tag
                    and node_value.tag == "tag:yaml.org,2002:null"
                    and node_value.value == "null"):
                continue
            if not (isinstance(node_key, ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, ScalarNode)
                    and not node_value.style):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node


def dump(
        data,
        stream=None,
        default_style=None,
        default_flow_style=False,
        canonical=None,
        indent=None,
        width=None,
        allow_unicode=None,
        line_break=None,
        encoding=None,
        explicit_start=None,
        explicit_end=None,
        version=None,
        tags=None,
        sort_keys=True,
        allow_null_tag=True,
):
    """
    Serialize a sequence of Python objects into a YAML stream.
    If stream is None, return the produced string instead.

    For the greater part, this is taken from the PyYAML library but
    only supports the Dumper implementation of this module,
    which adds a allow_null_tag keyword for optionally suppress nodes with
    null values in the output stream.

    Furthermore node keys formated in snake case will be tranformed to camel case.
    Meaning, remove all _ characters and replace the subsequent character after
    each _ with its upper case equivalent.
    e.g. `api_version: v1` will transformed to `apiVersion: v1`.
    """
    getvalue = None
    if stream is None:
        import io

        if encoding is None:
            stream = io.StringIO()
        else:
            stream = io.BytesIO()
        getvalue = stream.getvalue
    dumper = Dumper(
        stream,
        default_style=default_style,
        default_flow_style=default_flow_style,
        canonical=canonical,
        indent=indent,
        width=width,
        allow_unicode=allow_unicode,
        line_break=line_break,
        encoding=encoding,
        version=version,
        tags=tags,
        explicit_start=explicit_start,
        explicit_end=explicit_end,
        sort_keys=sort_keys,
        allow_null_tag=allow_null_tag,
    )
    try:
        dumper.open()
        dumper.represent(data.to_dict())
        dumper.close()
    finally:
        dumper.dispose()
    if getvalue:
        return getvalue()

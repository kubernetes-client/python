# Introduction to Kubernetes Patch Types
In Kubernetes, patches are a way to make updates or changes to resources (like Pods, ConfigMaps, Deployments, etc.) without having to replace the entire resource. Patches allow you to modify specific parts of a resource while leaving the rest unchanged.

## Types of Kubernetes Patches

There are several types of patches that Kubernetes supports:

1. JSON Merge Patch (Standard JSON Patch)
2. Strategic Merge Patch
3. JSON Patch
4. Apply Patch (Server-Side Apply)

## 1. JSON Merge Patch
- JSON Merge Patch is based on the concept of merging JSON objects. When you apply a patch, you only need to specify the changes you want to make. Kubernetes will take your partial update and merge it with the existing resource.

- This patch type is simple and works well when you need to update fields, such as changing a value or adding a new key.


### Example Scenario:
Imagine you have a Kubernetes Pod resource that looks like this:

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: nginx
      image: nginx:1.14
    - name: redis
      image: redis:5
```
Now, you want to change the image of the nginx container from nginx:1.14 to nginx:1.16. Instead of sending the entire resource, you can send only the part you want to change, like this:
```
{
  "spec": {
    "containers": [
      {
        "name": "nginx",
        "image": "nginx:1.16"
      }
    ]
  }
}
```

When you send this patch to Kubernetes:

It will replace the image of the nginx container with the new one (nginx:1.16).
It will leave the redis container unchanged, because it's not included in the patch.

### Example Code (Python):
```
from kubernetes import client, config

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    namespace = "default"
    name = "mypod"

    patch = {
        "spec": {
            "containers": [
                {
                    "name": "nginx",
                    "image": "nginx:1.16"
                }
            ]
        }
    }

    v1.patch_namespaced_pod(name=name, namespace=namespace, body=patch, content_type="application/merge-patch+json")

if __name__ == "__main__":
    main()

```

### After the  JSON Merge patch

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: nginx
      image: nginx:1.16  # Updated image version
    - name: redis
      image: redis:5  # Unchanged
```


## 2. Strategic Merge Patch
Strategic Merge Patch is another type of patching mechanism, mostly used in Kubernetes, that allows updates to objects in a way that is more aware of the structure and semantics of the resource being modified. It is strategic because it understands the structure of the object, rather than blindly replacing it, and applies the changes in a smart way.
- The patch itself is typically a JSON or YAML object, which contains the fields to be updated
-	**Adds New Fields:** You can use it to add new fields or modify existing ones without affecting the rest of the object.
- **Handle Lists or Arrays:** When dealing with lists (e.g., arrays or dictionaries), Strategic Merge Patch handles merging and updates intelligently.

### Example of Strategic Merge Patch:
let's suppose we have a yaml file Target Resource (Kubernetes ConfigMap):

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  key1: value1
  key2: value2
  list1:
    - item1
    - item2

```

Strategic Merge Patch
```
data:
  key1: updated_value1  # Update key1
  key3: value3          # Add new key3
  list1:
    - item1
    - item2
    - item3             # Add item3 to list1

```

Result after Strategic Merge Patch

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  key1: updated_value1  # key1 is updated
  key2: value2          # key2 is unchanged
  key3: value3          # key3 is added
  list1:
    - item1
    - item2
    - item3             # item3 is added to list1


```


## 3. JSON Patch
- JSON Patch is a standard format that specifies a way to apply updates to a JSON document. Instead of sending a new or merged version of the object, JSON Patch describes how to modify the object step-by-step.
- Operation-Based: A JSON Patch is an array of operations that describe modifications to a target JSON object.
- Ideal when you need to perform multiple, specific operations on resource fields (e.g., replacing a value, adding new fields, or deleting specific values).

### Patch Structure:
A JSON Patch is an array of operations. Each operation is an object with:
•	op: The operation type (e.g., add, remove, replace, etc.).
•	path: A JSON Pointer string (defined in RFC 6901) that specifies the location in the document to apply the operation.
•	value: (Optional) The new value to apply (used with operations like add, replace, or test).
•	from: (Optional) Used in operations like move and copy to specify the source path.

### Supported Operations for JSON Patch

#### 1. **add**
- Adds a value to a specified path.
- If the path already exists, it adds the value to a list or object.

Example:
```json
{ "op": "add", "path": "/a/b/c", "value": "foo" }
```

#### 2. **remove**
- Removes the value at the specified path.

Example:
```json
{ "op": "remove", "path": "/a/b/c" }
```

#### 3. **replace**
- Replaces the value at the specified path.
- Functionally similar to remove followed by add.

Example:
```json
{ "op": "replace", "path": "/a/b/c", "value": "bar" }
```

#### 4. **move**
- Moves a value from one path to another.

Example:
```json
{ "op": "move", "from": "/a/b/c", "path": "/x/y/z" }
```

#### 5. **copy**
- Copies a value from one path to another.

Example:
```json
{ "op": "copy", "from": "/a/b/c", "path": "/x/y/z" }
```

#### 6. **test**
- Tests whether a value at a specified path matches a given value.
- Used for validation in transactional updates.

Example:
```json
{ "op": "test", "path": "/a/b/c", "value": "foo" }
```

---

#### Example: Applying a JSON Patch

##### Target JSON Document:
```json
{
  "a": {
    "b": {
      "c": "foo"
    }
  },
  "x": {
    "y": "bar"
  }
}
```

##### JSON Patch:
```json
[
  { "op": "replace", "path": "/a/b/c", "value": "baz" },
  { "op": "add", "path": "/a/d", "value": ["new", "value"] },
  { "op": "remove", "path": "/x/y" }
]
```

##### Result:
```json
{
  "a": {
    "b": {
      "c": "baz"
    },
    "d": ["new", "value"]
  },
  "x": {}
}
```


## 4. Apply Patch (Server-Side Apply)
Server-Side Apply is a feature in Kubernetes that allows you to declaratively update resources by specifying their desired state. It provides an intuitive and robust way to manage resources without having to manually modify every field. It tracks which fields belong to which manager, which helps prevent conflicts when multiple clients (such as different controllers or users) update the same resource.

Key Features:
- Declarative Management: You provide the desired final state, and Kubernetes ensures the actual state matches it.
- Conflict Detection: Ensures changes from different clients don’t conflict with each other.
- Field Ownership: Kubernetes tracks which client or manager owns which fields of a resource.

##### Example Scenario:

You have a ConfigMap and want to update certain keys but leave others unchanged.
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-config
  namespace: default
data:
  key1: value1
  key2: value2
```
**Goal:**
- You want to update key2 to new_value2 and 
- add a new key key3 with a value value3. 
- leave key1 unchanged

##### Apply Patch YAML(Desired State):
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-config
  namespace: default
data:
  key2: new_value2   # Update existing key
  key3: value3       # Add new key

```

##### Resulting ConfigMap (after apply):
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-config
  namespace: default
data:
  key1: value1          # Remains unchanged
  key2: new_value2      # Updated value
  key3: value3          # New key added

```






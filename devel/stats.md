# Download Statistics

Pypi stores download information in a [BigQuery public dataset](https://bigquery.cloud.google.com/dataset/the-psf:pypi). It can be queried to get detailed information about downloads. For example, to get the number of downloads per version, you can run this query:

```sql
SELECT
  file.version,
  COUNT(*) as total_downloads,
FROM
  TABLE_DATE_RANGE(
    [the-psf:pypi.downloads],
    TIMESTAMP("20161120"),
    CURRENT_TIMESTAMP()
  )
where file.project == "kubernetes"
GROUP BY
  file.version
ORDER BY
  total_downloads DESC
LIMIT 20
```

More example queries can be found [here](https://gist.github.com/alex/4f100a9592b05e9b4d63)

Reference: https://mail.python.org/pipermail/distutils-sig/2016-May/028986.html


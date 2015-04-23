import django.db


def _get(f, v):
    try:
        f, key = f
        v = f.rel.to.objects.get(**{key: v}).pk if v else None
    except TypeError:
        pass
    return f.get_attname(), v


@django.db.transaction.atomic
def load(cls, rows):
    fs = {c.column: cls.XLSX_2_FIELDS.get(c.value) for c in rows[0]}
    cls.objects.all().delete()
    cls.objects.bulk_create([
        cls(**dict(_get(fs[c.column], c.value) for c in r if fs[c.column]))
        for r in rows[1:]
        ]
    )

import django.db


class Iterator:

    def __init__(self, remap, preprocess):
        self.remap = remap
        self.preprocess = preprocess

    def __call__(self, rows, _get):
        fs = {c.column: self.remap(c.value) for c in rows[0]}
        for r in rows[1:]:
            dr = dict(_get(fs[c.column], c.value) for c in r if fs[c.column])
            self.preprocess(dr)
            yield dr


def _get(f, v):
    try:
        f, key = f
        v = f.rel.to.objects.get(**{key: v}).pk if v else None
    except TypeError:
        pass
    return f.get_attname(), v


@django.db.transaction.atomic
def load(model, rows, preprocess=lambda dr: None):
    model.objects.all().delete()
    it = Iterator(remap=model.XLSX_2_FIELDS.get, preprocess=preprocess)
    model.objects.bulk_create([model(**r) for r in it(rows, _get)])

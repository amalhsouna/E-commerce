from core import ma


class CategorySchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)

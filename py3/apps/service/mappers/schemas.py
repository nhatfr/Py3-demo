from marshmallow import Schema, fields, validate, ValidationError

"""
File store mapping and validate data using marshmallow
"""


def must_not_be_blank(data):
    if not data or data is None:
        raise ValidationError('Is Blank')


class StoreForCategorySchema(Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=10, max=100)])


class CategorySchema(Schema):
    name = fields.String(required=True, validate=must_not_be_blank)
    description = fields.String(required=True, validate=[validate.Length(min=1, max=5)])
    store = fields.Nested(StoreForCategorySchema, many=True)

    class Meta:
        ordered = True


class StoreSchema(Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=10, max=100)])
    description = fields.Str(required=False, validate=[validate.Length(max=200)])
    phone_number = fields.Integer()
    address = fields.Str(required=False, validate=[validate.Length(max=200)])

    class Meta:
        ordered = True


class ServiceSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(validate=lambda n: n > 0)
    store = fields.Nested(StoreSchema, only=('name', 'description'))

    class Meta:
        ordered = True

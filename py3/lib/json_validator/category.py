import colander


class Category(colander.TupleSchema):
    name = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(colander.String())


cstruct ={
            "description": "this is descriptions",
            "name": "Software"
        }
schema = Category()
schema.deserialize(cstruct)
from marshmallow import Schema, fields


class UserDTO(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required =True)
    age = fields.Int(required=True)
    email = fields.String(required=True)
    def __str__(self):
        return '[id=' + str(self.id) + ' name=' + self.name + " age=" + str(self.age) + ']'

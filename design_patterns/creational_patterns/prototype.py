import copy


class Prototype:
    def __init__(self):
        self.parent = None

    def clone(self, parent):
        self.parent = parent


class MyObject(Prototype):
    def __init__(self, some_init, list_of_objects, proto_object):
        self.some_init = some_init
        self.list_of_objects = list_of_objects
        self.proto_object = proto_object

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_proto_object = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_init, some_list_of_objects, some_proto_object)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_proto_object = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_init, some_list_of_objects, some_proto_object)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
proto = Prototype()
component = MyObject(23, list_of_objects, proto)
proto.clone(component)
shallow_copied_component = copy.copy(component)

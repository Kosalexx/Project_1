class IncorrectDataError(Exception):
    ...


class Element(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next_val = None

    def _validate_data(self, data):
        if data not in range(1, 10000):
            raise IncorrectDataError("Data must be in range from 1 to 10000.")

    @property
    def data(self):
        """Gets the value of data."""
        return self._data

    @property
    def next_val(self):
        """Gets the value of next item of the Element."""
        return self._next

    @data.setter
    def data(self, value: int):
        """Sets the value of data."""
        self._validate_data(value)
        self._data = value

    @next_val.setter
    def next_val(self, nextval):
        """Sets the value of next item of the Element."""
        self._next = nextval

    # Comparison methods
    def __eq__(self, other) -> bool:
        if not isinstance(other, Element):
            raise ValueError("The second object must be Element.")
        return self.data == other.data

    def __gt__(self, other) -> bool:
        if not isinstance(other, Element):
            raise ValueError("The second object must be Element.")
        return self.data > other.data

    def __ge__(self, other) -> bool:
        if not isinstance(other, Element):
            raise ValueError("The second object must be Element.")
        return self.data >= other.data


class LinkedList(object):
    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        cur_element = self.head
        counter = 0
        while cur_element is not None:
            counter += 1
            cur_element = cur_element.next_val
        return counter

    def __iter__(self):
        self.cur_el = self.head
        return self

    def __next__(self):
        if self.cur_el is None:
            raise StopIteration
        result = self.cur_el.data
        self.cur_el = self.cur_el.next_val
        return result

    def append(self, element: int) -> None:
        """ Adds element to the end of LinkedList."""
        new_element = Element(element)
        cur_element = self.head
        if self.head is None:
            self.head = new_element
            return
        while cur_element.next_val is not None:
            cur_element = cur_element.next_val
        cur_element.next_val = new_element

    def println(self) -> None:
        """Prints the value of LinkedList as a list."""
        cur_element = self.head
        res_list = []
        while cur_element is not None:
            res_list.append(cur_element.data)
            cur_element = cur_element.next_val
        print(res_list)

    def reverse(self) -> None:
        """Reverses the order of the LinkedList."""
        prev_el = None
        cur_el = self.head
        next_el = None
        while cur_el is not None:
            next_el = cur_el.next_val
            cur_el.next_val = prev_el
            prev_el = cur_el
            cur_el = next_el
        self.head = prev_el


el1 = Element(4)
el2 = Element(3)
el3 = Element(4)
print(el1 == el2)
print(el1 == el3)
print(el1 != el2)
print(el1 != el3)
print(el1 > el2)
print(el2 < el2)
print(el1 <= el2)
print(el1 >= el2)
print(el1 >= el2)

my_list = LinkedList()
my_list.append(2)
my_list.append(2)
my_list.append(6)
my_list.append(20)
my_list.append(4)

print(len(my_list))
my_list.println()
my_list.reverse()
my_list.println()

for i in my_list:
    print(i)

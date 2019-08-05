from collections import namedtuple


def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """
    object_fields = []
    values = []

    for rec in records:
        for field in rec._fields:
            object_fields.append(field)
        for vars in rec:
            values.append(vars)
    Patient = namedtuple('Patient', object_fields)
    instance = Patient._make(values)
    return instance


if __name__ == '__main__':
    PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
    personal_details = PersonalDetails(date_of_birth='06-04-1972')

    Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
    complexion = Complexion(eye_color = 'Blue', hair_color='Black')

    print(merge(personal_details, complexion))

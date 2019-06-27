from collections import namedtuple

def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """
    object_fields = []
    values = []
    Patient = namedtuple('Patient', object_fields)
    for rec in records:
        for f in rec._fields:
            object_fields.append(f)
        print(dir(rec))
        values.append(rec)
    Patient._make(values)



PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')

Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

print(merge(personal_details, complexion))

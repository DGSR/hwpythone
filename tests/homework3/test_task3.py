from homework3.task3 import Filter, make_filter


def test_Filter():
    positive_even = Filter(lambda a: a % 2 == 0,
                           lambda a: a > 0,
                           lambda a: isinstance(a, int))
    assert positive_even.apply(range(100)) == list(range(2, 99, 2))


def test_make_filter():
    sample_data = [
     {
         'name': 'Bill',
         'last_name': 'Gilbert',
         'occupation': 'was here',
         'type': 'person',
     },
     {
         'is_dead': True,
         'kind': 'parrot',
         'type': 'bird',
         'name': 'polly'
     },
     {
         'is_dead': False,
         'kind': 'parrot',
         'type': 'bird',
         'name': 'pollytech'
     }
    ]
    assert make_filter(name='polly', type='bird').apply(sample_data) == [
        {'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}
        ]

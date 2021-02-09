from django.template import Context, Template



t = Template("My name is {{ person.first_name }}.")
d = {"person": {"first_name": "Joe", "last_name": "Johnson"}}
print(t.render(Context(d)))

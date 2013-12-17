import parse

def assert_template(item, name, data):
	assert item[0] == 'template'
	assert item[1] == name
	assert len(item[2]) == len(data)
	for key, val in data.items():
		assert key in item[2]
		assert item[2][key] == val

def assert_text(item, value):
	assert item[0] == 'text'
	assert item[1] == value

def test_parse_template_then_text():
	test = "{{parent | param = with nested {{child | test}} }}some text"

	items = parse.parse(test)
	assert len(items) == 2
	
	assert_template(items[0], 'parent', { 'param': 'with nested {{child | test}}'})
	assert_text(items[1], 'some text')
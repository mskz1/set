from src.xs_section import make_all_section_db, xs_section_property

db = make_all_section_db()

sec_name = 'H24'
a = xs_section_property(sec_name, 'An')
print(a)


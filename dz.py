import pymorphy2


text = "���� ���� ����"
text_split = text.split(" ")

morph = pymorphy2.MorphAnalyzer()

for a in text_split:
	parse = morph.parse(a)[0] #����� morph.analyzer ���������� ��� �������, � [0] �������
	result = parse.normalized #���������� �����, �� �������� ��� [0] ����
	sklon = parse.inflect({"gent"})
	lex = parse.lexeme 
	print("������� ������", parse)
	print("�������������: ", result)
	print("��������� � �����������: ", sklon)
	print("�������: ", lex)
	print("**************************************")
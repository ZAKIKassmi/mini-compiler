from semantic_analyzer import analyze_semantic

def test_lexical_no_valid_one():
  res = analyze_semantic("Hello")
  expected_output = "Lexical error: Sentence contains unknown token."
  assert res["message"] == expected_output

def test_lexical_no_valid_two():
  res = analyze_semantic("فَلَيتَ دونَكَ بِيداً دونَهَا يدُ")
  expected_output = "Lexical error: Sentence contains unknown token."
  assert res["message"] == expected_output

def test_lexical_no_valid_three():
  res = analyze_semantic("ضَ")
  expected_output = "Lexical error: Sentence contains unknown token."
  assert res["message"] == expected_output

def test_lexical_valid_one():
  res = analyze_semantic("بمَا مَضَى أمْ بأمْرٍ فيكَ تجْديدُ")
  expected_output = "Verification Result: Valid phrase."
  assert res["message"] == expected_output

#'NOUN', 'NOUN', 'NOUN', 'VERB', 'PREPOSITION', 'NOUN'

def test_syntax_one():
  res = analyze_semantic("بمَا مَضَى بأمْرٍ أمْ فيكَ تجْديدُ")
  expected_output = "Syntax error: Invalid token order."
  assert res["message"] == expected_output

def test_syntax_two():
  res = analyze_semantic("أمْ فيكَ أمْ")
  expected_output = "Syntax error: Invalid token order."
  assert res["message"] == expected_output

def test_semantic_one():
  res = analyze_semantic("بمَا مَضَى بأمْرٍ")
  expected_output = "Semantic error: it does not make sense"
  assert res["message"] == expected_output

def test_semantic_two():
  res = analyze_semantic("بمَا")
  expected_output = "Semantic error: it does not make sense"
  assert res["message"] == expected_output
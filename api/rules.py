import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = (
    'NOUN',
    'VERB',
    'PREPOSITION',
    'ADJECTIVE',
    'CONJUNCTION',
    'IDENTIFIER'
)

def t_NOUN(t):
    r'تجْديدُ|الأحِبّةُ|فالبَيْداءُ|دونَهُمُ|دونَكَ|بِيداً|دونَهَا|بِيدُ|العُلى|حَرْفٌ|قَيْدودُ|عيدُ|عيدٌ|بأيّةِ|حالٍ|بأمْرٍ|كُؤوسكُما|هَمٌّ|تَسهيدُ|صَخْرَةٌ|المُدامُ|الأغَارِيدُ|اللّوْنِ|حَبيبُ|النّفسِ|الدّنْيا|خَازِناً|أمْوَالي|المَوَاعِيدُ|القِرى|الترْحالِ|الرّجالِ|اللّسانِ|مُعانَقَةً|سَيفي|الجُودُ|المَوْتُ|نَفساً|عَبدُ|السّوْءِ|سَيّدَهُ|مصرَ|الخَصِيّ|الآبِقِينَ|الحُرّ|العَبْدُ|نَوَاطِيرُ|ثَعَالِبِها|العَنَاقيدُ|ثِيابِ|العَصا|العَبيدَ|زَمَنٍ|النّاسَ|البَيْضاءِ|العَضَاريطُ|زادي|القَدرِ|خُطّةً|المَهْرِيّةُ|المَنِيّةَ|الذّلّ|قِنْديدُ|الأسْوَدَ|المَخصِيّ|مكرُمَةً|البِيضُ|النّخّاسِ|الفِلْسَينِ|اللّئَامِ|الغِيدُ|رَوْنَقِهِ|أشْبَاهُ|الأمَاليدُ|الدّهْرُ|كُوَيْفِيرٌ|كبدي|قَلبي|شَيْئاً|عَينٌ|جِيدُ|كُؤوسِكُمَا|أصَخْرَةٌ|هَمٌّ|هَذي|سَاقِيَيَّ|هَذِي|كُمَيْتَ|مَفقُودُ|الدّنْيَا|أني|أخَمْرٌ|الفُحُولَ|بكَذّابِينَ|القِرَى|الغَنيّ|جُودُهُمُ|الأيدي|جودُ|نفوسِهِمُ|ضَيْفُهُمُ|نَتْنِهَا|تَمْهِيدُ|عُودُ|يَدِهِ|فالحُرّ|مِصرٍ|ثِيَابِ|بأخٍ|مَوْلُودُ|لِحُرٍّ|العَبْدَ|لأنْجَاسٌ|العَصَا|عَبْدٌ|مِثْلَ|أبي|مَشْفَرُهُ|الرّعاديد|ويْلُمِّهَا|ويْلُمِّ|قَابِلِهَا|لِمِثْلِها|مَقْصُودُ|طَعْمَ|المَوْتِ|شَارِبُهُ|أقَوْمُهُ|آبَاؤهُ|الصِّيدُ|إمَامَ|وَيَداً|الخِصْيةُ'
    t.value = t.value
    return t

def t_VERB(t):
    r'عُدتَ|فَلَيتَ|تجُبْ|مَضَى|أرَدْتُ|لَقيتُ|أمْسَيْتُ|نَزَلْتُ|يَقبضُ|اغتَالَ|خَانَهُ|نَامَتْ|بَشِمْنَ|تَفنى|تَشْتَرِ|أحْسَبُ|تَوَهّمْتُ|فُقِدوا|تُطيعُهُ|يأكُلُ|يُمسِكني|يَترُكِ|تُتَيّمُهُ|تُحَرّكُني|وَجَدْتُهَا|أعْجَبُهُ|كانوا|هُ|أحْيَا|لَيْسَ|خُلِقَ|كُنتُ|صَارَ|يُسِيءُ|لَذّ|يُقالَ|وَكَانَ|عَلّمَ'
    t.value = t.value
    return t

def t_PREPOSITION(t):
    r'بمَا|إنّي|يا|أمْ|فيكَ|أمّا|لَوْلا|لم|بي|ما|بهَا|وَلا|في|مِنْ|أنَا|عَنْ|لا|لي|وَلا|ذا|منَ|مِنْهُ|إلى|من|أكُلّمَا|لَهُ|قَدْ|بِهَا|ذي|لكَيْ|مَنْ|مَعَهُ|إذا|إلاّ|عِنْدَ|عَنِ'
    t.value = t.value
    return t

def t_ADJECTIVE(t):
    r'أجوبُ|وَجْنَاءُ|جَرْداءُ|صَافِيَةً|شاكٍ|مَحْسُودُ|مُثْرٍ|محْدُودُ|كَذّابِينَ|مُسْتَعْبَدٌ|مَعْبُودُ|صَالِحٍ|مَنَاكِيدُ|مَوْجودُ|دامِيَةً|مَحْمُودُ|المَثْقُوبَ|جَوْعانُ|القُودُ|عَظيمُ|أرْوَحَ|أطيَبَ|مَرْدودُ'
    t.value = t.value
    return t

def t_CONJUNCTION(t):
    r'وَ|فَ|أوْ|إنّ|إنّي|ولا|ها|هْوَ|هِ|ني|لَوْ|أنّ'
    t.value = t.value
    return t


# Ignore whitespace
t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[^\s]+'
    return t

def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Create lexer
lexer = lex.lex()

# Parser rules
def p_sentence(p):
    '''
    sentence : PREPOSITION VERB PREPOSITION NOUN PREPOSITION NOUN
             | NOUN NOUN NOUN VERB PREPOSITION NOUN
             | PREPOSITION NOUN NOUN NOUN
             | VERB NOUN NOUN NOUN NOUN
             | CONJUNCTION PREPOSITION CONJUNCTION VERB NOUN NOUN NOUN
             | PREPOSITION VERB ADJECTIVE NOUN NOUN
             | PREPOSITION NOUN PREPOSITION VERB PREPOSITION PREPOSITION ADJECTIVE PREPOSITION
             | ADJECTIVE NOUN PREPOSITION ADJECTIVE NOUN
             | VERB ADJECTIVE PREPOSITION NOUN NOUN
             | NOUN NOUN NOUN NOUN
             | CONJUNCTION NOUN PREPOSITION NOUN NOUN
             | ADJECTIVE VERB PREPOSITION NOUN CONJUNCTION VERB
             | PREPOSITION VERB NOUN PREPOSITION NOUN PREPOSITION NOUN
             | NOUN VERB NOUN PREPOSITION NOUN
             | PREPOSITION NOUN NOUN PREPOSITION NOUN
             | PREPOSITION PREPOSITION NOUN NOUN CONJUNCTION NOUN
             | NOUN PREPOSITION PREPOSITION PREPOSITION PREPOSITION VERB
             | NOUN NOUN PREPOSITION NOUN NOUN
             | PREPOSITION VERB NOUN NOUN ADJECTIVE
             | VERB CONJUNCTION NOUN NOUN NOUN
             | PREPOSITION PREPOSITION VERB PREPOSITION NOUN CONJUNCTION VERB
             | NOUN PREPOSITION PREPOSITION ADJECTIVE PREPOSITION VERB ADJECTIVE
             | VERB ADJECTIVE ADJECTIVE NOUN NOUN
             | PREPOSITION NOUN CONJUNCTION NOUN NOUN
             | PREPOSITION NOUN CONJUNCTION PREPOSITION NOUN ADJECTIVE
             | NOUN NOUN PREPOSITION NOUN CONJUNCTION NOUN
             | PREPOSITION NOUN CONJUNCTION PREPOSITION VERB PREPOSITION NOUN
             | PREPOSITION VERB NOUN NOUN PREPOSITION NOUN
             | PREPOSITION CONJUNCTION PREPOSITION NOUN PREPOSITION NOUN NOUN
             | PREPOSITION VERB NOUN NOUN NOUN
             | CONJUNCTION VERB CONJUNCTION PREPOSITION PREPOSITION NOUN NOUN
             | VERB NOUN NOUN NOUN PREPOSITION
             | NOUN ADJECTIVE CONJUNCTION NOUN ADJECTIVE
             | VERB NOUN NOUN PREPOSITION NOUN
             | CONJUNCTION PREPOSITION VERB CONJUNCTION PREPOSITION VERB NOUN
             | NOUN VERB NOUN ADJECTIVE NOUN
             | CONJUNCTION CONJUNCTION VERB PREPOSITION NOUN NOUN NOUN
             | PREPOSITION VERB NOUN PREPOSITION CONJUNCTION NOUN PREPOSITION
             | CONJUNCTION NOUN NOUN ADJECTIVE
             | PREPOSITION VERB VERB CONJUNCTION VERB PREPOSITION NOUN
             | VERB PREPOSITION PREPOSITION CONJUNCTION NOUN CONJUNCTION CONJUNCTION ADJECTIVE
             | CONJUNCTION VERB CONJUNCTION NOUN PREPOSITION VERB
             | CONJUNCTION CONJUNCTION NOUN NOUN NOUN ADJECTIVE
             | CONJUNCTION CONJUNCTION PREPOSITION NOUN ADJECTIVE NOUN
             | VERB PREPOSITION NOUN NOUN
    '''
    pass


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
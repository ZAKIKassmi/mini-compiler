from rules import lexer, parser
from pydantic import BaseModel




def analyze_semantic(proverb_input):
    # Set the input for the lexer
    lexer.input(proverb_input)

    # List to store tokens
    tokens = []

    # Get tokens until the end of the input
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
        #st.write(f"Token: {token.type} -> {token.value}")  

    # Valid token type combinations
    valid_order = [
             ['PREPOSITION', 'VERB', 'PREPOSITION', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['NOUN', 'NOUN', 'NOUN', 'VERB', 'PREPOSITION', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'NOUN', 'NOUN'],
             ['VERB', 'NOUN', 'NOUN', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'PREPOSITION', 'VERB', 'PREPOSITION', 'PREPOSITION', 'ADJECTIVE', 'PREPOSITION'],
             ['ADJECTIVE', 'NOUN', 'PREPOSITION', 'ADJECTIVE', 'NOUN'],
             ['VERB', 'ADJECTIVE', 'PREPOSITION', 'NOUN', 'NOUN'],
             ['NOUN','NOUN','NOUN','NOUN'],
             ['PREPOSITION', 'VERB', 'NOUN', 'PREPOSITION', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['NOUN', 'VERB', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['PREPOSITION', 'PREPOSITION', 'NOUN', 'NOUN', 'CONJUNCTION', 'NOUN'],
             ['NOUN', 'PREPOSITION', 'PREPOSITION', 'PREPOSITION', 'PREPOSITION', 'VERB'],
             ['NOUN', 'NOUN', 'PREPOSITION', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'VERB', 'NOUN', 'NOUN', 'ADJECTIVE'],
             ['VERB', 'CONJUNCTION', 'NOUN', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'PREPOSITION', 'VERB', 'PREPOSITION', 'NOUN', 'CONJUNCTION', 'VERB'],
             ['NOUN', 'PREPOSITION', 'PREPOSITION', 'ADJECTIVE', 'PREPOSITION', 'VERB', 'ADJECTIVE'],
             ['VERB', 'ADJECTIVE', 'ADJECTIVE', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'CONJUNCTION', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'CONJUNCTION', 'PREPOSITION', 'NOUN', 'ADJECTIVE'],
             ['NOUN', 'NOUN', 'PREPOSITION', 'NOUN', 'CONJUNCTION', 'NOUN'],
             ['PREPOSITION', 'NOUN', 'CONJUNCTION', 'PREPOSITION', 'VERB', 'PREPOSITION', 'NOUN'],
             ['PREPOSITION', 'VERB', 'NOUN', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['PREPOSITION', 'CONJUNCTION', 'PREPOSITION', 'NOUN', 'PREPOSITION', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'VERB', 'NOUN', 'NOUN', 'NOUN'],
             ['CONJUNCTION', 'VERB', 'CONJUNCTION', 'PREPOSITION', 'PREPOSITION', 'NOUN', 'NOUN'],
             ['VERB', 'NOUN', 'NOUN', 'NOUN', 'PREPOSITION'],
             ['NOUN', 'ADJECTIVE', 'CONJUNCTION', 'NOUN', 'ADJECTIVE'],
             ['VERB', 'NOUN', 'NOUN', 'PREPOSITION', 'NOUN'],
             ['CONJUNCTION', 'PREPOSITION', 'VERB', 'CONJUNCTION', 'PREPOSITION', 'VERB', 'NOUN'],
             ['NOUN', 'VERB', 'NOUN', 'ADJECTIVE', 'NOUN'],
             ['CONJUNCTION', 'CONJUNCTION', 'VERB', 'PREPOSITION', 'NOUN', 'NOUN', 'NOUN'],
             ['PREPOSITION', 'VERB', 'NOUN', 'PREPOSITION', 'CONJUNCTION', 'NOUN', 'PREPOSITION'],
             ['CONJUNCTION', 'NOUN', 'NOUN', 'ADJECTIVE'],
             ['PREPOSITION', 'VERB', 'VERB', 'CONJUNCTION', 'VERB', 'PREPOSITION', 'NOUN'],
             ['VERB', 'PREPOSITION', 'PREPOSITION', 'CONJUNCTION', 'NOUN', 'CONJUNCTION', 'CONJUNCTION', 'ADJECTIVE'],
             ['CONJUNCTION', 'VERB', 'CONJUNCTION', 'NOUN', 'PREPOSITION', 'VERB'],
             ['CONJUNCTION', 'CONJUNCTION', 'NOUN', 'NOUN', 'NOUN', 'ADJECTIVE'],
             ['CONJUNCTION', 'CONJUNCTION', 'PREPOSITION', 'NOUN', 'ADJECTIVE', 'NOUN'],
             ['VERB', 'PREPOSITION', 'NOUN', 'NOUN'],
             ['ADJECTIVE', 'VERB', 'PREPOSITION', 'NOUN', 'CONJUNCTION', 'VERB'],
             ['PREPOSITION', 'VERB', 'ADJECTIVE', 'NOUN', 'NOUN'],
             ['CONJUNCTION', 'PREPOSITION', 'CONJUNCTION', 'VERB', 'NOUN', 'NOUN', 'NOUN'],
             ['CONJUNCTION', 'NOUN', 'PREPOSITION', 'NOUN', 'NOUN'],
    ]

    # Predefined "bayts" with their token values
    bayts = {
    ('عيدٌ', 'بأيّةِ', 'حالٍ', 'عُدتَ', 'يا', 'عيدُ'): "عيدٌ بأيّةِ حالٍ عُدتَ يا عيدُ",
    ('بمَا', 'مَضَى', 'أمْ', 'بأمْرٍ', 'فيكَ', 'تجْديدُ'): "بمَا مَضَى أمْ بأمْرٍ فيكَ تجْديدُ",
    ('أمّا', 'الأحِبّةُ', 'فالبَيْداءُ', 'دونَهُمُ'): "أمّا الأحِبّةُ فالبَيْداءُ دونَهُمُ",
    ('فَلَيتَ', 'دونَكَ', 'بِيداً', 'دونَهَا', 'بِيدُ'): "فَلَيتَ دونَكَ بِيداً دونَهَا بِيدُ",
    ('لَوْلا', 'العُلى', 'لم', 'تجُبْ', 'بي', 'ما', 'أجوبُ', 'بهَا'): "لَوْلا العُلى لم تجُبْ بي ما أجوبُ بهَا",
    ('وَجْنَاءُ', 'حَرْفٌ', 'وَلا', 'جَرْداءُ', 'قَيْدودُ'): "وَجْنَاءُ حَرْفٌ وَلا جَرْداءُ قَيْدودُ",
    ('وَكَانَ', 'أطيَبَ', 'مِنْ', 'سَيفي', 'مُعانَقَةً'): "وَكَانَ أطيَبَ مِنْ سَيفي مُعانَقَةً",
    ('أشْبَاهُ', 'رَوْنَقِهِ', 'الغِيدُ', 'الأمَاليدُ'): "أشْبَاهُ رَوْنَقِهِ الغِيدُ الأمَاليدُ",
    ('لم', 'يَترُكِ', 'الدّهْرُ', 'مِنْ', 'قَلبي', 'وَلا', 'كبدي'): "لم يَترُكِ الدّهْرُ مِنْ قَلبي وَلا كبدي",
    ('شَيْئاً', 'تُتَيّمُهُ', 'عَينٌ', 'وَلا', 'جِيدُ'): "شَيْئاً تُتَيّمُهُ عَينٌ وَلا جِيدُ",
    ('يا', 'سَاقِيَيَّ', 'أخَمْرٌ', 'في', 'كُؤوسكُما'): "يا سَاقِيَيَّ أخَمْرٌ في كُؤوسكُما",
    ('أمْ', 'في', 'كُؤوسِكُمَا', 'هَمٌّ','وَ', 'تَسهيدُ'): "أمْ في كُؤوسِكُمَا هَمٌّ وَ تَسهيدُ",
    ('أصَخْرَةٌ', 'أنَا', 'ما', 'لي', 'لا', 'تُحَرّكُني'): "أصَخْرَةٌ أنَا، ما لي لا تُحَرّكُني",
    ('هَذِي', 'المُدامُ', 'وَلا', 'هَذي', 'الأغَارِيدُ'): "هَذِي المُدامُ وَلا هَذي الأغَارِيدُ",
    ('إذا', 'أرَدْتُ', 'كُمَيْتَ', 'اللّوْنِ', 'صَافِيَةً'): "إذا أرَدْتُ كُمَيْتَ اللّوْنِ صَافِيَةً",
    ('وَجَدْتُهَا','وَ', 'حَبيبُ', 'النّفسِ', 'مَفقُودُ'): "وَجَدْتُهَا وَ حَبيبُ النّفسِ مَفقُودُ",
    ('ما','ذا', 'لَقيتُ', 'منَ', 'الدّنْيَا','وَ', 'أعْجَبُهُ'): "ماذا لَقيتُ منَ الدّنْيَا وَ أعْجَبُهُ",
    ('أني', 'بمَا', 'أنَا', 'شاكٍ', 'مِنْ','هُ', 'مَحْسُودُ'): "أني بمَا أنَا شاكٍ مِنْهُ مَحْسُودُ",
    ('أمْسَيْتُ', 'أرْوَحَ', 'مُثْرٍ', 'خَازِناً', 'وَيَداً'): "أمْسَيْتُ أرْوَحَ مُثْرٍ خَازِناً وَيَداً",
    ('أنَا', 'الغَنيّ','وَ', 'أمْوَالي', 'المَوَاعِيدُ'): "أنَا الغَنيّ وَأمْوَالي المَوَاعِيدُ",
    ('إنّي', 'نَزَلْتُ', 'بكَذّابِينَ', 'ضَيْفُهُمُ'): "إنّي نَزَلْتُ بكَذّابِينَ ضَيْفُهُمُ",
    ('عَنِ', 'القِرَى','وَ', 'عَنِ', 'الترْحالِ', 'محْدُودُ'): "عَنِ القِرَى وَعَنِ الترْحالِ محْدُودُ",
    ('جودُ', 'الرّجالِ', 'من', 'الأيدي','وَ', 'جُودُهُمُ'): "جودُ الرّجالِ من الأيدي وَجُودُهُمُ",
    ('منَ', 'اللّسانِ','فَ', 'لا', 'كانوا', 'وَلا', 'الجُودُ'): "منَ اللّسانِ فَلا كانوا وَلا الجُودُ",
    ('ما', 'يَقبضُ', 'المَوْتُ', 'نَفساً', 'من', 'نفوسِهِمُ'): "ما يَقبضُ المَوْتُ نَفساً من نفوسِهِمُ",
    ('إلاّ','وَ', 'في', 'يَدِهِ', 'مِنْ', 'نَتْنِهَا', 'عُودُ'): "إلاّ وَفي يَدِهِ مِنْ نَتْنِهَا عُودُ",
    ('أكُلّمَا', 'اغتَالَ', 'عَبدُ', 'السّوْءِ', 'سَيّدَهُ'): "أكُلّمَا اغتَالَ عَبدُ السّوْءِ سَيّدَهُ",
    ('أوْ', 'خَانَهُ','فَ', 'لَهُ', 'في', 'مصرَ', 'تَمْهِيدُ'): "أوْ خَانَهُ فَلَهُ في مصرَ تَمْهِيدُ",
    ('صَارَ', 'الخَصِيّ', 'إمَامَ', 'الآبِقِينَ', 'بِهَا'): "صَارَ الخَصِيّ إمَامَ الآبِقِينَ بِهَا",
    ('فالحُرّ', 'مُسْتَعْبَدٌ','وَ', 'العَبْدُ', 'مَعْبُودُ'): "فالحُرّ مُسْتَعْبَدٌ وَالعَبْدُ مَعْبُودُ",
    ('نَامَتْ', 'نَوَاطِيرُ', 'مِصرٍ', 'عَنْ', 'ثَعَالِبِها'): "نَامَتْ نَوَاطِيرُ مِصرٍ عَنْ ثَعَالِبِها",
    ('فَ','قَدْ', 'بَشِمْنَ','وَ', 'ما', 'تَفنى', 'العَنَاقيدُ'): "فَقَدْ بَشِمْنَ وَما تَفنى العَنَاقيدُ",
    ('العَبْدُ', 'لَيْسَ', 'لِحُرٍّ', 'صَالِحٍ', 'بأخٍ'): "العَبْدُ لَيْسَ لِحُرٍّ صَالِحٍ بأخٍ",
    ('لَوْ','أنّ', 'هُ', 'في', 'ثِيَابِ', 'الحُرّ', 'مَوْلُودُ'): "لَوْ أنّهُ في ثِيَابِ الحُرّ مَوْلُودُ",
    ('لا', 'تَشْتَرِ', 'العَبْدَ', 'إلاّ','وَ', 'العَصَا', 'مَعَهُ'): "لا تَشْتَرِ العَبْدَ إلاّ وَالعَصَا مَعَهُ",
    ('إنّ', 'العَبيدَ', 'لأنْجَاسٌ', 'مَنَاكِيدُ'): "إنّ العَبيدَ لأنْجَاسٌ مَنَاكِيدُ",
    ('ما', 'كُنتُ','أحْسَبُ', 'ني', 'أحْيَا', 'إلى', 'زَمَنٍ'): "ما كُنتُ أحْسَبُني أحْيَا إلى زَمَنٍ",
    ('يُسِيءُ', 'بي', 'في','هِ', 'عَبْدٌ', 'وَ','هْوَ' ,'مَحْمُودُ'): "يُسِيءُ بي فيهِ عَبْدٌ وَهْوَ مَحْمُودُ",
    ('ولا', 'تَوَهّمْتُ', 'أنّ', 'النّاسَ', 'قَدْ', 'فُقِدوا'): "ولا تَوَهّمْتُ أنّ النّاسَ قَدْ فُقِدوا",
    ('وَ','أنّ', 'مِثْلَ', 'أبي', 'البَيْضاءِ', 'مَوْجودُ'): "وَأنّ مِثْلَ أبي البَيْضاءِ مَوْجودُ",
    ('وَ','أنّ', 'ذا', 'الأسْوَدَ', 'المَثْقُوبَ', 'مَشْفَرُهُ'): "وَأنّ ذا الأسْوَدَ المَثْقُوبَ مَشْفَرُهُ",
    ('تُطيعُهُ', 'ذي', 'العَضَاريطُ', 'الرّعاديد'): "تُطيعُهُ ذي العَضَاريطُ الرّعاديد",
    ('جَوْعانُ', 'يأكُلُ', 'مِنْ', 'زادي','وَ', 'يُمسِكني'): "جَوْعانُ يأكُلُ مِنْ زادي وَيُمسِكني",
    ('لكَيْ', 'يُقالَ', 'عَظيمُ', 'القَدرِ', 'مَقْصُودُ'): "لكَيْ يُقالَ عَظيمُ القَدرِ مَقْصُودُ",
    ('ويْلُمِّهَا', 'خُطّةً', 'ويْلُمِّ', 'قَابِلِهَا'): "ويْلُمِّهَا خُطّةً ويْلُمِّ قَابِلِهَا",
    ('لِمِثْلِها', 'خُلِقَ', 'المَهْرِيّةُ', 'القُودُ'): "لِمِثْلِها خُلِقَ المَهْرِيّةُ القُودُ",
    ('وَ','عِنْدَ','ها', 'لَذّ', 'طَعْمَ', 'المَوْتِ', 'شَارِبُهُ'): "وَعِنْدَها لَذّ طَعْمَ المَوْتِ شَارِبُهُ",
    ('إنّ', 'المَنِيّةَ', 'عِنْدَ', 'الذّلّ', 'قِنْديدُ'): "إنّ المَنِيّةَ عِنْدَ الذّلّ قِنْديدُ",
    ('مَنْ', 'عَلّمَ', 'الأسْوَدَ', 'المَخصِيّ', 'مكرُمَةً'): "مَنْ عَلّمَ الأسْوَدَ المَخصِيّ مكرُمَةً",
    ('أقَوْمُهُ', 'البِيضُ', 'أمْ', 'آبَاؤهُ', 'الصِّيدُ'): "أقَوْمُهُ البِيضُ أمْ آبَاؤهُ الصِّيدُ",
    }


    token_types = [token.type for token in tokens]
    token_values = tuple(token.value for token in tokens)

    if any(token.type == 'IDENTIFIER' for token in tokens):

        return {
            "is_error":True,
            "message": "Lexical error: Sentence contains unknown token.",
        }
    elif not any(token_types == order[:len(token_types)] for order in valid_order):

        return {
            "is_error":True,
            "message":"Syntax error: Invalid token order.",
        }
    elif token_values in bayts:

        return {
            "is_error":False,
            "message":"Verification Result: Valid phrase.",
        }
        
    else:
        return {
            "is_error":True,
            "message":"Semantic error: it does not make sense",
        }
        
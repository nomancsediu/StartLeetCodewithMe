# Comprehensive Bengali translation data
# This replaces HuggingFace datasets for deployment compatibility

TRANSLITERATION_DATA = {
    # Pronouns
    'ami': 'আমি', 'tumi': 'তুমি', 'se': 'সে', 'apni': 'আপনি', 'amra': 'আমরা', 'tomra': 'তোমরা',
    'tara': 'তারা', 'ei': 'এই', 'oi': 'ওই', 'eta': 'এটা', 'ota': 'ওটা', 'keu': 'কেউ', 'kichhu': 'কিছু',
    
    # Question words
    'kemon': 'কেমন', 'ki': 'কি', 'keno': 'কেন', 'kothay': 'কোথায়', 'kokhon': 'কখন', 'kivabe': 'কিভাবে',
    'koto': 'কত', 'kar': 'কার', 'kake': 'কাকে', 'kader': 'কাদের', 'kon': 'কোন', 'kothai': 'কোথায়',
    
    # Adjectives
    'bhalo': 'ভালো', 'valo': 'ভালো', 'kharap': 'খারাপ', 'sundor': 'সুন্দর', 'boro': 'বড়', 'choto': 'ছোট',
    'notun': 'নতুন', 'purano': 'পুরানো', 'gorom': 'গরম', 'thanda': 'ঠান্ডা', 'lal': 'লাল', 'nil': 'নীল',
    'holud': 'হলুদ', 'sobuj': 'সবুজ', 'kalo': 'কালো', 'sada': 'সাদা', 'dhushor': 'ধূসর', 'mishti': 'মিষ্টি',
    'tita': 'তিতা', 'jhal': 'ঝাল', 'nonta': 'নোনতা', 'shokto': 'শক্ত', 'norom': 'নরম', 'druto': 'দ্রুত',
    'dhire': 'ধীরে', 'uccha': 'উচ্চ', 'nichu': 'নিচু', 'lomba': 'লম্বা', 'khato': 'খাটো', 'mota': 'মোটা',
    'chikon': 'চিকন', 'gabhir': 'গভীর', 'otol': 'অতল', 'shorol': 'সরল', 'kothin': 'কঠিন', 'sohoj': 'সহজ',
    
    # Verbs - Present
    'achi': 'আছি', 'acho': 'আছো', 'ache': 'আছে', 'achhen': 'আছেন', 'achhi': 'আছি', 'thaki': 'থাকি',
    'thako': 'থাকো', 'thake': 'থাকে', 'thaken': 'থাকেন', 'kori': 'করি', 'koro': 'করো', 'kore': 'করে',
    'karen': 'করেন', 'korchi': 'করছি', 'korcho': 'করছো', 'korche': 'করছে', 'korchen': 'করছেন',
    'jai': 'যাই', 'jao': 'যাও', 'jay': 'যায়', 'jan': 'যান', 'jachi': 'যাচ্ছি', 'jacho': 'যাচ্ছো',
    'jache': 'যাচ্ছে', 'jachen': 'যাচ্ছেন', 'asi': 'আসি', 'asho': 'আসো', 'ashe': 'আসে', 'ashen': 'আসেন',
    'aschi': 'আসছি', 'ascho': 'আসছো', 'asche': 'আসছে', 'aschen': 'আসছেন', 'khai': 'খাই', 'khao': 'খাও',
    'khay': 'খায়', 'khan': 'খান', 'khachi': 'খাচ্ছি', 'khacho': 'খাচ্ছো', 'khache': 'খাচ্ছে', 'khachen': 'খাচ্ছেন',
    
    # Verbs - Future
    'korbo': 'করব', 'korbe': 'করবে', 'korben': 'করবেন', 'jabo': 'যাব', 'jabe': 'যাবে', 'jaben': 'যাবেন',
    'asbo': 'আসব', 'asbe': 'আসবে', 'asben': 'আসবেন', 'khabo': 'খাব', 'khabe': 'খাবে', 'khaben': 'খাবেন',
    'dekhbo': 'দেখব', 'dekhbe': 'দেখবে', 'dekhben': 'দেখবেন', 'bolbo': 'বলব', 'bolbe': 'বলবে', 'bolben': 'বলবেন',
    'sunbo': 'শুনব', 'sunbe': 'শুনবে', 'sunben': 'শুনবেন', 'porbo': 'পড়ব', 'porbe': 'পড়বে', 'porben': 'পড়বেন',
    'likhbo': 'লিখব', 'likhbe': 'লিখবে', 'likhben': 'লিখবেন', 'ghurbo': 'ঘুরব', 'ghurbe': 'ঘুরবে', 'ghurben': 'ঘুরবেন',
    
    # Verbs - Past
    'korlam': 'করলাম', 'korle': 'করলে', 'korlo': 'করল', 'korlen': 'করলেন', 'gelam': 'গেলাম', 'gele': 'গেলে',
    'gelo': 'গেল', 'gelen': 'গেলেন', 'elam': 'এলাম', 'ele': 'এলে', 'elo': 'এল', 'elen': 'এলেন',
    'khelam': 'খেলাম', 'khele': 'খেলে', 'khelo': 'খেল', 'khelen': 'খেলেন', 'dekhlam': 'দেখলাম', 'dekhle': 'দেখলে',
    'dekhlo': 'দেখল', 'dekhlen': 'দেখলেন', 'bollam': 'বললাম', 'bolle': 'বললে', 'bollo': 'বলল', 'bollen': 'বললেন',
    'sunlam': 'শুনলাম', 'sunle': 'শুনলে', 'sunlo': 'শুনল', 'sunlen': 'শুনলেন', 'porlam': 'পড়লাম', 'porle': 'পড়লে',
    'porlo': 'পড়ল', 'porlen': 'পড়লেন', 'likhlam': 'লিখলাম', 'likhle': 'লিখলে', 'likhlo': 'লিখল', 'likhlen': 'লিখলেন',
    
    # Numbers
    'ek': 'এক', 'dui': 'দুই', 'tin': 'তিন', 'char': 'চার', 'panch': 'পাঁচ', 'choy': 'ছয়', 'saat': 'সাত',
    'aat': 'আট', 'noy': 'নয়', 'dosh': 'দশ', 'egaro': 'এগারো', 'baro': 'বারো', 'tero': 'তেরো', 'chouddo': 'চৌদ্দ',
    'ponero': 'পনেরো', 'sholo': 'ষোলো', 'shotero': 'সতেরো', 'atharo': 'আঠারো', 'unish': 'উনিশ', 'bish': 'বিশ',
    
    # Family
    'baba': 'বাবা', 'ma': 'মা', 'bhai': 'ভাই', 'bon': 'বোন', 'dada': 'দাদা', 'dadi': 'দাদি', 'nana': 'নানা',
    'nani': 'নানি', 'chacha': 'চাচা', 'chachi': 'চাচি', 'mama': 'মামা', 'mami': 'মামি', 'fufa': 'ফুফা', 'fufu': 'ফুফু',
    'khala': 'খালা', 'khalu': 'খালু', 'chele': 'ছেলে', 'meye': 'মেয়ে', 'bou': 'বউ', 'jamai': 'জামাই',
    
    # Body parts
    'matha': 'মাথা', 'chokh': 'চোখ', 'nak': 'নাক', 'mukh': 'মুখ', 'kan': 'কান', 'gola': 'গলা', 'hat': 'হাত',
    'pa': 'পা', 'angul': 'আঙুল', 'chul': 'চুল', 'dant': 'দাঁত', 'jiv': 'জিভ', 'buk': 'বুক', 'pet': 'পেট',
    
    # Food
    'bhat': 'ভাত', 'roti': 'রুটি', 'dal': 'ডাল', 'torkari': 'তরকারি', 'mach': 'মাছ', 'mangsho': 'মাংস',
    'dim': 'ডিম', 'dudh': 'দুধ', 'pani': 'পানি', 'cha': 'চা', 'coffee': 'কফি', 'mishti': 'মিষ্টি', 'fol': 'ফল',
    
    # Time
    'shokal': 'সকাল', 'dupur': 'দুপুর', 'bikel': 'বিকেল', 'shondha': 'সন্ধ্যা', 'rat': 'রাত', 'din': 'দিন',
    'mash': 'মাস', 'bochor': 'বছর', 'ghonta': 'ঘন্টা', 'minute': 'মিনিট', 'second': 'সেকেন্ড', 'ekhon': 'এখন',
    'age': 'আগে', 'pore': 'পরে', 'kal': 'কাল', 'ajke': 'আজকে', 'gotokal': 'গতকাল', 'porshukaal': 'পরশুকাল'
}

TRANSLATION_DATA = {
    # Basic phrases
    'i am': 'আমি', 'you are': 'তুমি', 'he is': 'সে', 'she is': 'সে', 'we are': 'আমরা', 'they are': 'তারা',
    'how are': 'কেমন আছেন', 'what is': 'কি', 'where is': 'কোথায়', 'when is': 'কখন', 'why is': 'কেন',
    'who is': 'কে', 'which is': 'কোনটা', 'how much': 'কত', 'how many': 'কতগুলো', 'what time': 'কয়টা বাজে',
    
    # Emotions & feelings
    'i love': 'আমি ভালোবাসি', 'i like': 'আমি পছন্দ করি', 'i want': 'আমি চাই', 'i need': 'আমার দরকার',
    'i have': 'আমার আছে', 'i know': 'আমি জানি', 'i think': 'আমি মনে করি', 'i see': 'আমি দেখি',
    'i hear': 'আমি শুনি', 'i feel': 'আমি অনুভব করি', 'i understand': 'আমি বুঝি', 'i remember': 'আমি মনে রাখি',
    'i forget': 'আমি ভুলে যাই', 'i believe': 'আমি বিশ্বাস করি', 'i hope': 'আমি আশা করি', 'i wish': 'আমি ইচ্ছা করি',
    
    # Greetings
    'good morning': 'সুপ্রভাত', 'good night': 'শুভ রাত্রি', 'good evening': 'শুভ সন্ধ্যা', 'good afternoon': 'শুভ দুপুর',
    'hello there': 'হ্যালো', 'see you': 'দেখা হবে', 'take care': 'যত্ন নিও', 'be well': 'ভালো থেকো',
    
    # Politeness
    'thank you': 'ধন্যবাদ', 'you are welcome': 'স্বাগতম', 'excuse me': 'মাফ করবেন', 'i am sorry': 'আমি দুঃখিত',
    'please help': 'দয়া করে সাহায্য করুন', 'no problem': 'কোন সমস্যা নেই', 'of course': 'অবশ্যই',
    
    # Descriptions
    'very good': 'খুব ভালো', 'very bad': 'খুব খারাপ', 'very nice': 'খুব সুন্দর', 'very big': 'খুব বড়',
    'very small': 'খুব ছোট', 'very hot': 'খুব গরম', 'very cold': 'খুব ঠান্ডা', 'too much': 'অনেক বেশি',
    'too little': 'অনেক কম', 'just right': 'ঠিক আছে', 'not enough': 'যথেষ্ট নয়', 'more than': 'এর চেয়ে বেশি',
    
    # Actions
    'come here': 'এখানে এসো', 'go there': 'ওখানে যাও', 'sit down': 'বসো', 'stand up': 'দাঁড়াও',
    'come in': 'ভিতরে এসো', 'go out': 'বাইরে যাও', 'turn on': 'চালু কর', 'turn off': 'বন্ধ কর',
    'open it': 'খুলে দাও', 'close it': 'বন্ধ কর', 'pick up': 'তুলে নাও', 'put down': 'রেখে দাও',
    
    # Time expressions
    'right now': 'এখনই', 'later on': 'পরে', 'before this': 'এর আগে', 'after this': 'এর পরে',
    'long time': 'অনেক সময়', 'short time': 'অল্প সময়', 'all day': 'সারাদিন', 'all night': 'সারারাত',
    'every day': 'প্রতিদিন', 'sometimes': 'মাঝে মাঝে', 'always': 'সবসময়', 'never': 'কখনো না',
    
    # Questions
    'what happened': 'কি হয়েছে', 'where are you': 'তুমি কোথায়', 'when will you': 'তুমি কখন',
    'why did you': 'তুমি কেন', 'how did you': 'তুমি কিভাবে', 'who told you': 'তোমাকে কে বলেছে',
    'which one': 'কোনটা', 'how long': 'কতক্ষণ', 'how far': 'কত দূর', 'how old': 'কত বয়স',
    
    # Common responses
    'i dont know': 'আমি জানি না', 'i dont understand': 'আমি বুঝি না', 'i cant': 'আমি পারি না',
    'i can': 'আমি পারি', 'maybe': 'হয়তো', 'definitely': 'অবশ্যই', 'probably': 'সম্ভবত',
    'of course not': 'অবশ্যই না', 'thats right': 'ঠিক বলেছো', 'thats wrong': 'ভুল বলেছো',
    
    # Family & relationships
    'my family': 'আমার পরিবার', 'my friend': 'আমার বন্ধু', 'my brother': 'আমার ভাই', 'my sister': 'আমার বোন',
    'my father': 'আমার বাবা', 'my mother': 'আমার মা', 'my wife': 'আমার স্ত্রী', 'my husband': 'আমার স্বামী',
    
    # Places
    'at home': 'বাড়িতে', 'at school': 'স্কুলে', 'at work': 'কাজে', 'in market': 'বাজারে',
    'in hospital': 'হাসপাতালে', 'in office': 'অফিসে', 'on road': 'রাস্তায়', 'in car': 'গাড়িতে'
}
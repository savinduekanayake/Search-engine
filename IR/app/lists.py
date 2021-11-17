syn_rel_subjects = ["විෂයයන්", "පථයන්", "මාතෘකා"]
syn_position = ["තනතුර", "ධුර", "ධුරය", "නිලය", "පදවිය", "තරාතිරම", "තානාන්තරය", "තැන"]
syn_party = ["කණ්ඩායම", "පක්ෂය", "පාර්ශ්වය", "කණ්ඩායම"]
syn_districts = ["දිස්ත්‍රික්කය","දිස්ික්කය","පළාත", "ප්‍රදේශය"]
syn_contact = ["සම්බන්ධ", "දුරකථන" ,"අංකය", "ඇමතුම්"]
syn_participation = ["නියෝජනය", "සිටි", "සහභාගි", "වාර", " ගණන"]
synonym_list = [syn_position, syn_party, syn_districts, syn_rel_subjects, syn_contact, syn_participation]

fields_ori = ["position","party","district","related_subjects","contact_information","participated_in_parliament"]

syn_popularity=['හොඳම','ජනප්‍රිය','ප්‍රචලිත','ප්‍රසිද්ධ','හොදම','ජනප්‍රියම']
gte = ["වැඩි","වැඩිය","වැඩිපුර","වැඩියෙන්"]
lte = ["අඩුවෙන්","අඩු"]
times = ["වතාවකට","වරක්","වතාවක්","පාරක්","පාරකට","වතාවක","වරක","පාරක","වාරගනනක්"] + gte + lte

bio_list = ["පක්ෂයද",  "කොංග්‍රසයද", "බලවේගයද", "කූටිටනිද", "කොංග්‍රසයද", "පෙරමුණද", "කච්චිද", "පුළිකල්ද", "සන්ධානයද"]

stop_words = ['මහතා','මහත්මිය','කර', 'ගත', 'හැකි', 'මන්ත්රීවරු',"මන්ත්‍රීවරුන්", 'කරන','නියෝජනය','කළ']



districts =  [
        "කළුතර",
        "කෑගල්ල",
        "මහනුවර",
        "ජාතික",
        "ගාල්ල",
        "නුවරඑළිය",
        "මොණරාගල",
        "යාපනය",
        "ගම්පහ",
        "බදුල්ල",
        "කුරුණෑගල",
        "වන්නි",
        "මඩකලපුව",
        "අම්පාර",
        "හම්බන්තොට",
        "අනුරාධපුර",
        "රත්නපුර",
        "පුත්තලම",
        "ලැයිස්තුව",
        "ත්‍රිකුණාමලය",
        "පොළොන්නරුව",
        "මාතර",
        "කොළඹ",
        "මාතලේ"
    ]
positions = [
        "රාජ්‍ය අමාත්‍ය",
        "පාර්ලිමේන්තු මන්ත්‍රී",
        "අගමැති",
        "අමාත්‍ය"
    ]
parties = [
        "ජාතික කොංග්‍රසය",
        "සමගි ජන බලවේගය",
        "ඊලාම් ජනතා ප්‍රජාතන්ත්‍රවාදී පක්ෂය",
        "ශ්‍රී ලංකා නිදහස් පක්ෂය",
        "තමිල් මක්කල් තේසිය කූටිටනි",
        "අකිල ඉලංකෙයි තමිල් කොංග්‍රස්",
        "අපේ ජන බල පක්ෂය",
        "ශ්‍රී ලංකා මුස්ලිම් කොංග්‍රසය",
        "ශ්‍රී ලංකා පොදුජන පෙරමුණ",
        "ඉලංකෙයි තමිල් අරසු කච්චි",
        "තමිළ් මක්කල් විඩුදලෛප් පුළිකල්",
        "සමස්ථ ලංකා මහජන කොංග්‍රසය",
        "මුස්ලිම් ජාතික සන්ධානය",
        "ජාතික ජන බලවේගය"
    ]
related_subjects = [
        "ජාතික උරුමයන්, මාධ්‍ය හා ක්‍රීඩා",
        "වෙළඳ හා කර්මාන්ත",
        "සංහිඳියාව හා නැවත පදිංචි කිරීම",
        "කෘෂිකර්ම, වැවිලි, පශු සම්පත් සහ ධීවර",
        "ස්වභාවික සම්පත් හා පරිසර",
        "අයිතිවාසිකම්",
        "නගර සැලසුම්, යටිතල පහසුකම් හා ප්‍රවාහන ",
        "සුබසාධන හා සමාජ සේවා",
        "යුක්තිය, ආරක්ෂාව හා මහජන සාමය",
        "සෞඛ්‍ය",
        "අධ්‍යාපන",
        "ආර්ථික හා මුල්‍ය",
        "කම්කරු හා රැකියා",
        "ආණ්ඩුකරණ, පරිපාලන හා පාර්ලිමේන්තු කටයුතු",
        "තාක්ෂණ, සන්නිවේදන සහ බලශක්ති"
    ]
names = [
        "රාජවරෝදයම් සම්පන්දන්",
        "රාජිකා වික්‍රමසිංහ",
        "සාරතී දුෂ්මන්ත",
        "ජනක බණ්ඩාර තෙන්නකෝන්",
        "ජානක වක්කුඹුර",
        "තිස්ස අත්තනායක",
        "ජගත් පුෂ්පකුමාර",
        "විමලවීර දිසානායක",
        "අතුරලියේ රතන හිමි",
        "යදාමිණි ගුණවර්ධන",
        "ආර්. එම්. රංජිත් මද්දුම බණ්ඩාර",
        "ප්‍රේමලාල් ජයසේකර",
        "මිලාන් ජයතිලක",
        "විජයදාස රාජපක්‍ෂ",
        "ජගත් කුමාර",
        "ඩබ්ලිව්. එච්. එම්. ධර්මසේන",
        "ප්‍රමිත බණ්ඩාර තෙන්නකෝන්",
        "ප්‍රේම්නාත් සී. දොලවත්ත",
        "ගයන්ත කරුණාතිලක",
        "චමින්ද විජේසිරි",
        "සජිත් ප්‍රේමදාස",
        "විජිත බේරුගොඩ",
        "ප්‍රසන්න රණතුංග",
        "මුජිබුර් රහුමාන්",
        "වසන්ත යපාබණ්ඩාර",
        "වඩිවේල් සුරේෂ්",
        "වී. රාධක්‍රිෂ්ණන්",
        "වරුණ ලියනගේ",
        "උපුල් මහේන්ද්‍ර රාජපක්ෂ",
        "උද්දික ප්‍රේමරත්න",
        "විදුර වික්‍රමනායක",
        "උදයකාන්ත ගුණතිලක",
        "විමල් විරවංශ",
        "කුමාරසිරි රත්නායක",
        "කුලසිංහම් දිලීපන්",
        "උදයන කිරිඳිගොඩ",
        "යූ. කේ. සුමිත් උඩුකුඹුර",
        "වීරසුමන වීරසිංහ",
        "සරත් වීරසේකර",
        "තිස්ස විතාරණ",
        "කුමාර වෙල්ගම",
        "කරුණාදාස කොඩිතුවක්කු",
        "wijitha හේරත්",
        "කෝකිලා ගුණවර්ධන",
        "කෙහෙලිය රඹුක්වැල්ල",
        "කේ. කාදර් මස්තාන්",
        "වේලු කුමාර්",
        "ලලිත් එල්ලාවල",
        "කපිල අතුකෝරල",
        "කංචන විජේසේකර",
        "ජීවන් තොන්ඩමන්",
        "උපුල් ගලප්පත්ති",
        "කනක හේරත්",
        "ජයරත්න හේරත්",
        "කේ. පී. එස්. කුමාරසිරි",
        "ජයන්ත වීරසිංහ",
        "ජෝන් සෙනෙවිරත්න",
        "ඉසුරු දොඩන්ගොඩ",
        "නලින් ප්‍රනාන්දු",
        "කිංස් නෙල්සන්",
        "කවින්ද හේෂාන් ජයවර්ධන",
        "ජයන්ත කැටගොඩ",
        "ලක්ෂ්මන් කිරිඇල්ල",
        "රාජිත සේනාරත්න",
        "ඉම්තියාස් බාකීර් මාකාර්",
        "කබීර් හෂීම්",
        "ඉම්රාන් මහරූෆ්",
        "එච්. එම්. එම්. හරීස්",
        "එච්. නන්දසේන",
        "ජොන්ස්ටන් ප්‍රනාන්දු",
        "ජයන්ත සමරවීර",
        "ගුණතිලක රාජපක්‍ෂ",
        "නලින් බණ්ඩාර ජයමහ",
        "ගීතා සමන්මලී කුමාරසිංහ",
        "ගයාෂාන් නවනන්ද",
        "ගෝවින්දන් කරුණාකරම්",
        "ගෙවිදු කුමාරතුංග",
        "හර්ශණ සුපුන් රාජකරුණා",
        "හෙක්ටර් අප්පුහාමි",
        "ඉෂාක් රහුමාන්",
        "ඉන්දික අනුරුද්ධ හේරත්",
        "මුදිතා ප්‍රිිිශාන්ති",
        "හරිනි අමරසුරිය",
        "හේෂා විතානගේ",
        "හරින් ප්‍රනාන්දු",
        "ජේ. සී. අලවතුවල",
        "මර්ජාන් ෆලීල්",
        "මෛත්‍රීපාල   සිරිසේන",
        "හර්ෂ ද සිල්වා",
        "මහින්ද සමරසිංහ",
        "මොහාන් ප්‍රියදර්ශන ද සිල්වා",
        "මනෝ ගනේෂන්",
        "මංජුලා දිසානායක",
        "සුදර්ශන දෙනිපිටිය",
        "දිනේෂ් ගුණවර්ධන",
        "එම්. ඩබ්ලිව්. ඩී. සහන් ප්‍රදීප් විතාන",
        "බන්දුල ගුණවර්ධන",
        "එම්. එස්. තවුෆික්",
        "එම්. රාමේෂ්වරන්",
        "මයන්ත දිසානායක",
        "ටිරාන් අලස්",
        "එම්. උදයකුමාර්",
        "තිලක් රා‍ජපක්ෂ",
        "මදුර විතානගේ",
        "තවරාජා කලෙයි අරසන්",
        "තාරක බාලසූරිය",
        "තිසකුට්ටි ආරච්චි",
        "මොහමඩ් මුසම්මිල්",
        "තේනුක විදානගමගේ",
        "මනූෂ නානායක්කාර",
        "එම්. ඒ. සුමන්තිරන්",
        "ලොහාන් රත්වත්තේ",
        "ලසන්ත අලගියවන්න",
        "මහින්දානන්ද අළුත්ගමගේ",
        "මහින්ද යාපා අබේවර්ධන",
        "මහින්ද රාජපක්‍ෂ",
        "තලතා අතුකෝරල",
        "සිවනේසතුරෙයි චන්ද්‍රකාන්තන්",
        "මහින්ද අමරවීර",
        "සිරිපාල ගම්ලත්",
        "ශෂීන්ද්‍ර රාජපක්ෂ",
        "සුදත් මංජුල",
        "ෂාන් විජයලාල් ද සිල්වා",
        "ගාමිණී ලොකුගේ",
        "සිසිර ජයකොඩි",
        "තුෂාර ඉඳුනිල් අමරසේන",
        "සනත් නිශාන්ත",
        "සුජිත් පෙරේරා",
        "සෙල්වම් අඩෛක්කලනාදන්",
        "සිතා අරඹේපොල",
        "සුසිල් ප්‍රේමජයන්ත",
        "සාගර කාරියවසම්",
        "සුරේන් රාඝවන්",
        "සු. නෝගරාදලිංගම්",
        "සුදර්ශිනී ප්‍රනාන්‍දුපුල්ලේ",
        "සංජිව එදිරිමාන්න",
        "එස්. වියාලේන්ද්‍රන්",
        "සම්පත් අතුකෝරල",
        "සෙල්වරාජා කජේන්ද්‍රන්",
        "සිවඥානම් ශ්‍රීතරන්",
        "එස්. බී. දිසානායක",
        "ශෙහාන් සේමසිංහ",
        "ශාන්ත බණ්ඩාර",
        "එස්. එම්. එම්. මුෂාරෆ්",
        "රොෂාන් රණසිංහ",
        "සරත් ෆොන්සේකා",
        "සමන්ප්‍රිය හේරත්",
        "රිසාඩ් බදියුදීන්",
        "රෝහණ දිසානායක",
        "එස්.එම් චන්ද්‍රසේන",
        "රංජිත් බණ්ඩාර",
        "රංජිත් සියඹලාපිටිය",
        "රෝහිත අබේගුණවර්ධන",
        "එස්. එම්. මරික්කාර්",
        "ෆයිසාල් කාසිම්",
        "උදය ගම්මන්පිල",
        "ගාමිණී වලේබොඩ",
        "රංජන් රාමනායක",
        "දිලුම් අමුණුගම",
        "රෝහිණි කුමාරි විජේරත්න",
        "පාඨලී චම්පික රණවක",
        "දුමින්ද දිසානායක",
        "ධර්මලිංගම් සිද්ධාර්ථන්",
        "රෝහණ බණ්ඩාර",
        "රවුෆ් හකීම්",
        "ඩී. වීරසිංහ",
        "සාණක්කියා රාජපුත්තිරන් රාසමාණික්කම්",
        "ඩග්ලස් දේවානන්දා",
        "ඩයනා ගමගේ",
        "ඩි.වී චානක",
        "ඩලස් අලහප්පෙරුම",
        "චින්තක මායාදුන්න",
        "ජී. එල්. පීරිස්",
        "චරිත හේරත්",
        "දිලිප් වෙදආරච්චි",
        "චන්න  ජයසුමන",
        "ඩිලාන් පෙරේරා",
        "ජී. ජී. පොන්නම්බලම්",
        "ඉරාන් වික්‍රමරත්න",
        "ඩී. බී. හේරත්",
        "සී. වී. විග්නේෂ්වරන්",
        "අනුර කුමාර දිසානායක",
        "අසංක නවරත්න",
        "දයාසිරි ජයසේකර",
        "අනුප පස්කුවල්",
        "බී. වයි. ජී. රත්නසේකර",
        "අංගජන් රාමනාදන්",
        "ඒ. එල්. එම්. අතාඋල්ලා",
        "අශෝක ප්‍රියන්ත",
        "අරුන්දික ප්‍රනාන්දු",
        "චන්දිම වීරක්කොඩි",
        "අලි සබ්රි රහීම්",
        "අනුරාධ ජයරත්න",
        "අකිල එල්ලාවල",
        "නසීර් අහමඩ්",
        "අබ්දුල් හලීම්",
        "චාල්ස් නිර්මලනාදන්",
        "අ. අරවින්ද් කුමාර්",
        "චාමර සම්පත් දසනායක",
        "චමල් රාජපක්‍ෂ",
        "අනුර ප්‍රියදර්ශන යාපා",
        "පියංකර ජයරත්න",
        "පලනි දිගම්බරම්",
        "නිපුණ රණවක",
        "ප්‍රදීප් උඳුගොඩ",
        "බුද්ධික පතිරණ",
        "අමරකීර්ති අතුකෝරල",
        "සී. බී. රත්නායක",
        "ප්‍රසන්න රණවීර",
        "අජිත් රාජපක්‍ෂ",
        "අශෝක් අබේසිංහ",
        "නාලක බණ්ඩාර කෝට්ටේගොඩ",
        "නිමල් පියතිස්ස",
        "පියල් නිශාන්ත ද සිල්වා",
        "එම්. යූ. එම්. අලි සබ්රි",
        "අජිත් නිවාඩ් කබ්රාල්",
        "රමේශ් පතිරණ",
        "නොරෝෂන් පෙරේරා",
        "පවිත්‍රාදේවී වන්නිආරච්චි",
        "නාලක ගොඩහේවා",
        "නිමල් සිරිපාල ද සිල්වා",
        "වාසුදේව නානායක්කාර",
        "නිමල් ලාන්සා",
        "නාමල් රාජපක්‍ෂ"
    ]
all_lists = [positions, parties, districts, related_subjects]


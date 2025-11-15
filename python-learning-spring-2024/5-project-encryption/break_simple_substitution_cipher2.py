from simple_substitution_cipher import *
import string

# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)
# print(list(string.whitespace))

#             ABCDEFGHIJKLMNOPQRSTUVWXYZ
secret_key = "FEQHIDOPZASTGJBUVWCLMXYRKN"
assert("".join(sorted(list(secret_key)))==string.ascii_uppercase)

plain_text = """
The Allied victory in Sicily helped to bring about the surrender of
Italy. The terms of the Italian surrender were signed on 3 September
1943 and announced on the night of the 8th. Allied troops received the
news on shipboard while under way to invade Italy. Fighting did not
cease with the surrender. Instead, the Germans took over the country
with troops on the spot and sent reinforcements. The defeat of the
Germans in Italy would strengthen Allied control over the Mediterranean
shipping lanes and would provide air bases closer to targets in Germany
and enemy-occupied territory. The Allied troops in Italy would also
engage enemy troops which might otherwise have been employed against
the Russians.

On 3 September, elements of the British Eighth Army crossed into Italy
and advanced up the Italian toe in pursuit of the retreating Germans.
On 9 September the main assault was launched when an Anglo-American
force, part of the U. S. Fifth Army, landed on the beaches near
Salerno, south of Naples. Since the enemy had expected landings in the
vicinity of Naples and had disposed his forces accordingly, the Allies
encountered prompt and sustained resistance. By 15 September, however,
the Germans started to withdraw up the Italian Peninsula, pursued on
the west by the Fifth Army and on the east by the Eighth Army. The port
of Naples fell on 1 October and the Foggia airfields about the same
time.

After crossing the Volturno River against stiff resistance, the
Allies advanced to the Winter Line seventy-five miles south of Rome.
In bitterly cold weather the troops slogged through mud and snow to
breach the series of heavy defenses and advanced to the Gustav Line.
In midJanuary the main Fifth Army launched a new offensive across the
Rapido and Garigliano Rivers to pierce the Gustav Line and advance up
the Liri Valley toward Rome. Bridgeheads were secured across the rivers
and footholds were obtained in Cassino and surrounding hills, but no
break-through of the main German positions was effected. A few days
after the initial attack against the Gustav Line, an Anglo-American
amphibious force landed at Anzio and struck inland with the purpose
of compelling the Germans on the southern front to withdraw. But the
Allied beachhead force was contained by the enemy’s unexpectedly rapid
build-up and was hard pressed to stave off several fierce German
counterattacks.

After the Anzio front became stabilized and the effort to take Cassino
was abandoned, the AAI (Allied Armies in Italy) regrouped and launched
a new offensive on 11 May 1944. Fifth Army, led by French troops and
assisted by American troops, broke through the main German positions
in the Arunci Mountains west of the Garigliano River while the Eighth
Army advanced up the Liri Valley. A few days later the beachhead force
effected a junction with the troops from the southern front, and
advanced almost to Valmontone on Highway 6 before the axis of attack
was shifted to the northwest. After several unsuccessful attacks
toward Lanuvio and along the Albano road, the Fifth Army discovered an
unguarded point near Velletri, enveloped the German positions based on
the Alban Hills, and pushed on rapidly toward Rome, which fell on 4
June 1944 with the Germans in full retreat. Meanwhile preparations were
being rushed for an invasion of southern France by Allied troops, most
of them drawn from forces in Italy.
"""
# https://www.gutenberg.org/cache/epub/69911/pg69911.txt
#print(plain_text)

plain_text = plain_text.translate(str.maketrans('', '', string.punctuation + string.digits + string.whitespace + "’")).lower()
#print(plain_text)

# from collections import Counter
# print(Counter(plain_text))
# print(len(Counter(plain_text)))


cipher_text = encrypt_simple_substitution(plain_text, secret_key)
print(cipher_text)

from collections import Counter
#print(Counter(cipher_text))

bigram = []
for i in range(0,len(cipher_text)-1):
    bigram.append(cipher_text[i:i+2])
#print(Counter(bigram))

trigram = []
for i in range(0,len(cipher_text)-2):
    trigram.append(cipher_text[i:i+3])
#print(Counter(trigram))

# THE :  1.81        ERE :  0.31        HES :  0.24
# AND :  0.73        TIO :  0.31        VER :  0.24
# ING :  0.72        TER :  0.30        HIS :  0.24
# ENT :  0.42        EST :  0.28        OFT :  0.22
# ION :  0.42        ERS :  0.28        ITH :  0.21
# HER :  0.36

# 'lpi': 78, 'fjh': 28, 'pif': 15, 'ihl': 14, 'dlp': 14, 'zjo': 13, 


# TH :  2.71        EN :  1.13        NG :  0.89
# HE :  2.33        AT :  1.12        AL :  0.88
# IN :  2.03        ED :  1.08        IT :  0.88
# ER :  1.78        ND :  1.07        AS :  0.87
# AN :  1.61        TO :  1.07        IS :  0.86
# RE :  1.41        OR :  1.06        HA :  0.83
# ES :  1.32        EA :  1.00        ET :  0.76
# ON :  1.32        TI :  0.99        SE :  0.73

# 'lp': 101, 'pi': 91, 'fj': 76, 'iw': 63, 'ih': 52, 'zj': 52, 'if': 36, 'jh': 33, 'lf': 33, 
             

# E 529117365 12.10
# T 390965105 8.94
# A 374061888 8.55
# O 326627740 7.47
# I 320410057 7.33
# N 313720540 7.17
# S 294300210 6.73
# R 277000841 6.33
# H 216768975 4.96
# L 183996130 4.21

# 'i': 354, 'f': 248, 'l': 245, 'j': 217, 'b': 187, 'z': 184, 'w': 182, 'c': 165, 'p': 148, 'h': 130, 't': 108, 

#alphabet = ".....A.DEN.T...H.........."
alphabet = "JOSFBAMDENYTUZGHCXKLPQRVWI"
key      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += alphabet.lower()
key += key.lower()
reverse_substitution_table = str.maketrans(key, alphabet)
decrypted_text= cipher_text.translate(reverse_substitution_table)
print(decrypted_text)

#lpifttzihxzqlbwkzjczqztkpituihlbewzjofebmllpicmwwijhiwbdzlftklpiliwgcbdlpizlftzfjcmwwijhiwyiwiczojihbjciuligeiwfjhfjjbmjqihbjlpijzoplbdlpilpfttzihlwbbucwiqizxihlpijiycbjcpzuebfwhypztimjhiwyfklbzjxfhizlftkdzoplzjohzhjblqifciyzlplpicmwwijhiwzjclifhlpioiwgfjclbbsbxiwlpiqbmjlwkyzlplwbbucbjlpicublfjhcijlwizjdbwqigijlclpihidiflbdlpioiwgfjczjzlftkybmthclwijolpijfttzihqbjlwbtbxiwlpigihzliwwfjifjcpzuuzjotfjicfjhybmthuwbxzhifzwefcicqtbciwlblfwoilczjoiwgfjkfjhijigkbqqmuzihliwwzlbwklpifttzihlwbbuczjzlftkybmthftcbijofoiijigklwbbucypzqpgzoplblpiwyzcipfxieiijigutbkihfofzjcllpiwmcczfjcbjciuligeiwitigijlcbdlpiewzlzcpizoplpfwgkqwbccihzjlbzlftkfjhfhxfjqihmulpizlftzfjlbizjumwcmzlbdlpiwilwiflzjooiwgfjcbjciuligeiwlpigfzjfccfmtlyfctfmjqpihypijfjfjotbfgiwzqfjdbwqiufwlbdlpimcdzdlpfwgktfjhihbjlpieifqpicjifwcftiwjbcbmlpbdjfuticczjqilpiijigkpfhiruiqlihtfjhzjoczjlpixzqzjzlkbdjfuticfjhpfhhzcubcihpzcdbwqicfqqbwhzjotklpifttzicijqbmjliwihuwbgulfjhcmclfzjihwiczclfjqiekciuligeiwpbyixiwlpioiwgfjcclfwlihlbyzlphwfymulpizlftzfjuijzjcmtfumwcmihbjlpiyicleklpidzdlpfwgkfjhbjlpiifcleklpiizoplpfwgklpiubwlbdjfuticdittbjbqlbeiwfjhlpidboozffzwdzithcfebmllpicfgilzgifdliwqwbcczjolpixbtlmwjbwzxiwfofzjclclzddwiczclfjqilpifttzicfhxfjqihlblpiyzjliwtzjicixijlkdzxigzticcbmlpbdwbgizjezlliwtkqbthyiflpiwlpilwbbucctbooihlpwbmopgmhfjhcjbylbewifqplpiciwzicbdpifxkhidijcicfjhfhxfjqihlblpiomclfxtzjizjgzhafjmfwklpigfzjdzdlpfwgktfmjqpihfjiybddijczxifqwbcclpiwfuzhbfjhofwzotzfjbwzxiwclbuziwqilpiomclfxtzjifjhfhxfjqimulpitzwzxfttiklbyfwhwbgiewzhoipifhcyiwiciqmwihfqwbcclpiwzxiwcfjhdbblpbthcyiwibelfzjihzjqfcczjbfjhcmwwbmjhzjopzttcemljbewifslpwbmopbdlpigfzjoiwgfjubczlzbjcyfciddiqlihfdiyhfkcfdliwlpizjzlzftfllfqsfofzjcllpiomclfxtzjifjfjotbfgiwzqfjfgupzezbmcdbwqitfjhihflfjnzbfjhclwmqszjtfjhyzlplpiumwubcibdqbguittzjolpioiwgfjcbjlpicbmlpiwjdwbjllbyzlphwfyemllpifttziheifqppifhdbwqiyfcqbjlfzjiheklpiijigkcmjiruiqlihtkwfuzhemzthmufjhyfcpfwhuwiccihlbclfxibddcixiwftdziwqioiwgfjqbmjliwfllfqscfdliwlpifjnzbdwbjleiqfgiclfeztznihfjhlpiiddbwllblfsiqfcczjbyfcfefjhbjihlpiffzfttzihfwgziczjzlftkwiowbmuihfjhtfmjqpihfjiybddijczxibjgfkdzdlpfwgktihekdwijqplwbbucfjhfcczclihekfgiwzqfjlwbbucewbsilpwbmoplpigfzjoiwgfjubczlzbjczjlpifwmjqzgbmjlfzjcyiclbdlpiofwzotzfjbwzxiwypztilpiizoplpfwgkfhxfjqihmulpitzwzxfttikfdiyhfkctfliwlpieifqppifhdbwqiiddiqlihfamjqlzbjyzlplpilwbbucdwbglpicbmlpiwjdwbjlfjhfhxfjqihftgbcllbxftgbjlbjibjpzopyfkeidbwilpifrzcbdfllfqsyfccpzdlihlblpijbwlpyiclfdliwcixiwftmjcmqqiccdmtfllfqsclbyfwhtfjmxzbfjhftbjolpiftefjbwbfhlpidzdlpfwgkhzcqbxiwihfjmjomfwhihubzjljifwxittilwzijxitbuihlpioiwgfjubczlzbjcefcihbjlpiftefjpzttcfjhumcpihbjwfuzhtklbyfwhwbgiypzqpdittbjamjiyzlplpioiwgfjczjdmttwilwiflgifjypztiuwiufwflzbjcyiwieizjowmcpihdbwfjzjxfczbjbdcbmlpiwjdwfjqiekfttzihlwbbucgbclbdlpighwfyjdwbgdbwqiczjzlftk
#thealliedvictoryinsicilyhelpedtobringaboutthesurrenderofitalythetermsoftheitaliansurrenderweresignedonseptemberandannouncedonthenightofthethalliedtroopsreceivedthenewsonshipboardwhileunderwaytoinvadeitalyfightingdidnotceasewiththesurrenderinsteadthegermanstookoverthecountrywithtroopsonthespotandsentreinforcementsthedefeatofthegermansinitalywouldstrengthenalliedcontroloverthemediterraneanshippinglanesandwouldprovideairbasesclosertotargetsingermanyandenemyoccupiedterritorythealliedtroopsinitalywouldalsoengageenemytroopswhichmightotherwisehavebeenemployedagainsttherussiansonseptemberelementsofthebritisheightharmycrossedintoitalyandadvanceduptheitaliantoeinpursuitoftheretreatinggermansonseptemberthemainassaultwaslaunchedwhenanangloamericanforcepartoftheusfiftharmylandedonthebeachesnearsalernosouthofnaplessincetheenemyhadexpectedlandingsinthevicinityofnaplesandhaddisposedhisforcesaccordinglythealliesencounteredpromptandsustainedresistancebyseptemberhoweverthegermansstartedtowithdrawuptheitalianpeninsulapursuedonthewestbythefiftharmyandontheeastbytheeightharmytheportofnaplesfellonoctoberandthefoggiaairfieldsaboutthesametimeaftercrossingthevolturnoriveragainststiffresistancethealliesadvancedtothewinterlineseventyfivemilessouthofromeinbitterlycoldweatherthetroopssloggedthroughmudandsnowtobreachtheseriesofheavydefensesandadvancedtothegustavlineinmidjanuarythemainfiftharmylaunchedanewoffensiveacrosstherapidoandgariglianoriverstopiercethegustavlineandadvanceupthelirivalleytowardromebridgeheadsweresecuredacrosstheriversandfootholdswereobtainedincassinoandsurroundinghillsbutnobreakthroughofthemaingermanpositionswaseffectedafewdaysaftertheinitialattackagainstthegustavlineanangloamericanamphibiousforcelandedatan.ioandstruckinlandwiththepurposeofcompellingthegermansonthesouthernfronttowithdrawbutthealliedbeachheadforcewascontainedbytheenemysunexpectedlyrapidbuildupandwashardpressedtostaveoffseveralfiercegermancounterattacksafterthean.iofrontbecamestabili.edandtheefforttotakecassinowasabandonedtheaaialliedarmiesinitalyregroupedandlaunchedanewoffensiveonmayfiftharmyledbyfrenchtroopsandassistedbyamericantroopsbrokethroughthemaingermanpositionsinthearuncimountainswestofthegariglianoriverwhiletheeightharmyadvancedupthelirivalleyafewdayslaterthebeachheadforceeffectedajunctionwiththetroopsfromthesouthernfrontandadvancedalmosttovalmontoneonhighwaybeforetheaxisofattackwasshiftedtothenorthwestafterseveralunsuccessfulattackstowardlanuvioandalongthealbanoroadthefiftharmydiscoveredanunguardedpointnearvelletrienvelopedthegermanpositionsbasedonthealbanhillsandpushedonrapidlytowardromewhichfellonjunewiththegermansinfullretreatmeanwhilepreparationswerebeingrushedforaninvasionofsouthernfrancebyalliedtroopsmostofthemdrawnfromforcesinitaly

#secret_key_guess = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".translate(str.maketrans(alphabet,key))
#print(f"secret key:{secret_key}\nguess:     {secret_key_guess}")



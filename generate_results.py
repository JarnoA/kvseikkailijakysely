import os
import urllib.parse

# Data from translation files
en_data = {
    'unelmoijakorento': {
        'title': "You are a Dreamer Dragonfly!",
        'desc': "Your eyes have been opened to the wrongs of the world and you want to put right what's wrong. You are aware of your small size but don't let it get in the way of dreaming of change. You gather together with others to make your voice stronger. You're weighed down by inequality in the world, but you can also imagine a better future.",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank' rel='noopener noreferrer'>The European Solidarity Corps’ solidarity projects (in Finnish)</a> and <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank' rel='noopener noreferrer'>volunteer projects (in Finnish)</a> as well as <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank' rel='noopener noreferrer'>international trainings</a>.",
        'og_desc': "Your eyes have been opened to the wrongs of the world and you want to put right what's wrong. Find out which character you are!"
    },
    'kehittajakehraaja': {
        'title': "You are a Developer Moth!",
        'desc': "You know where you're headed, even if you haven't seen the whole route yet. You have a way of also getting others to try things that are not yet possible. As you flutter towards new networks, you dream about concepts and methods, seminars, influencing decision-makers and bringing different perspectives together. You turn project ideas into solutions to the problems that you face.",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-yhteistyohankkeet' target='_blank' rel='noopener noreferrer'>Erasmus+ partnerships for cooperation (in Finnish)</a> and <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank' rel='noopener noreferrer'>international trainings</a>.",
        'og_desc': "You know where you're headed, even if you haven't seen the whole route yet. Find out which character you are!"
    },
    'hallintomittari': {
        'title': "You are a Coordinating Caterpillar!",
        'desc': "You measure the world from where you are and can easily spot where your help is needed. You spring elegantly from manual to reporting form. You’re an important part of your population’s activities, as without you the wheels wouldn't turn or the ideas wouldn't reach the finish line.",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-hakuajat-ja-neuvonnat' target='_blank' rel='noopener noreferrer'>Briefings for Erasmus+ projects (in Finnish)</a> and <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukkojen-hakuajat-ja-neuvonnat' target='_blank' rel='noopener noreferrer'>European Solidarity Corps projects (in Finnish)</a>, <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank' rel='noopener noreferrer'>international trainings</a>.",
        'og_desc': "You measure the world from where you are and can easily spot where your help is needed. Find out which character you are!"
    },
    'seikkailijasirkka': {
        'title': "You are an Adventure Cricket!",
        'desc': "You've been involved in many things and have international experience, both abroad and at home. But your thirst for adventure hasn’t been sated yet, which is why you're already exploring the next opportunities to hop on a train and discover new landscapes to explore alone or with others! The moments when you see young people's own wings carrying them make up for all the emergency landings on the rocks.",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisotyontekijoiden-liikkuvuushanke' target='_blank' rel='noopener noreferrer'>Erasmus+ mobility of youth workers (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/discovereu' target='_blank' rel='noopener noreferrer'>DiscoverEU (in Finnish)</a>, <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank' rel='noopener noreferrer'>international trainings</a>.",
        'og_desc': "You've been involved in many things and have international experience. Find out which character you are!"
    },
    'rohkaisijakuoriainen': {
        'title': "You are an Encourager Beetle!",
        'desc': "You make sure that everyone feels heard and seen. You are ready to help others in every situation. You shower people with words of encouragement and know the paths and opportunities ahead. You give those around you, both young people and your colleagues, the courage to spread their wings in the face of new things!",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank' rel='noopener noreferrer'>The European Solidarity Corps’ solidarity projects (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorten-osallistumishanke' target='_blank' rel='noopener noreferrer'>Erasmus+ youth participation activities (in Finnish)</a>, <a href='https://www.oph.fi/en/internationalisation/eurodesk' target='_blank' rel='noopener noreferrer'>Eurodesk youth information network</a>.",
        'og_desc': "You make sure that everyone feels heard and seen. Find out which character you are!"
    },
    'osallisuuskimalainen': {
        'title': "You are a Participation Bee!",
        'desc': "You're inspired by young people finding new ways to make their voices heard. You've made it your business to make sure that every little creature in the garden has its place in the group. You know what kind of supported routes to the world are available, or at least you're determined to find out about them.",
        'info': "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank' rel='noopener noreferrer'>The European Solidarity Corps’ volunteer projects (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisovaihto' target='_blank' rel='noopener noreferrer'>Erasmus+ youth exchanges (in Finnish)</a>.",
        'og_desc': "You're inspired by young people finding new ways to make their voices heard. Find out which character you are!"
    }
}

sv_data = {
    'unelmoijakorento': {
        'title': "Du är en Drömmarslända!",
        'desc': "Dina ögon har öppnats för orättvisorna i världen, och du vill rätta till det som är fel. Du är medveten om din litenhet, men låter den inte hindra dig från att drömma om förändring. Du samlas med andra för att göra er röst starkare. Världens ojämlikhet tynger dina vingar, men samtidigt har du förmågan att föreställa dig en bättre framtid.",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-solidaritetsprojekt' target='_blank' rel='noopener noreferrer'>Europeiska solidaritetskårens solidaritetsprojekt</a> och <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-volontarverksamhet' target='_blank' rel='noopener noreferrer'>volontärprojekt</a> samt <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank' rel='noopener noreferrer'>internationella utbildningar</a>.",
        'og_desc': "Dina ögon har öppnats för orättvisorna i världen. Gör testet och ta reda på vilken karaktär du är!"
    },
    'kehittajakehraaja': {
        'title': "Du är en Idéspinnare!",
        'desc': "Du vet vart du är på väg, även om du ännu inte ser hela vägen. Du får också andra att pröva på sådant som ännu inte är möjligt. När du rör dig mot nya nätverk drömmer du om begrepp och metoder, seminarier, påverkan på beslutsfattare och om att föra samman olika perspektiv. Du spinner vidare projektidéer till lösningar på de problem du möter.",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/erasmus-ungdomssektorn-partnerskap-samarbete' target='_blank' rel='noopener noreferrer'>Erasmus+ partnerskap för samarbete</a> och <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank' rel='noopener noreferrer'>internationella utbildningar</a>.",
        'og_desc': "Du vet vart du är på väg. Gör testet och ta reda på vilken karaktär du är!"
    },
    'hallintomittari': {
        'title': "Du är en Förvaltningsmätare!",
        'desc': "Du mäter världen från din egen plats och ser snabbt var din insats behövs. Du rör dig smidigt från manualer till rapporteringsblanketter. Du är en viktig del av helheten, för utan dig skulle hjulen inte snurra och idéerna inte nå hela vägen fram.",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/ansokningstiderna-och-radgivning-ansokan' target='_blank' rel='noopener noreferrer'>Ansökningsrådgivningar för Erasmus+-projekt</a> och <a href='https://www.oph.fi/sv/program/ansokningstider-och-radgivningar-europeiska-solidaritetskaren' target='_blank' rel='noopener noreferrer'>projekt inom Europeiska solidaritetskåren</a>, <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank' rel='noopener noreferrer'>internationella utbildningar</a>.",
        'og_desc': "Du mäter världen från din egen plats och ser snabbt var din insats behövs. Gör testet och ta reda på vilken karaktär du är!"
    },
    'seikkailijasirkka': {
        'title': "Du är en Äventyrssyrsa!",
        'desc': "Du har varit med om mycket och har erfarenhet av internationella sammanhang både utomlands och i Finland. Din äventyrslust är dock fortfarande inte stillad – du utforskar redan nya möjligheter att hoppa på tåget och upptäcka nya miljöer där du kan spela ensam eller tillsammans med andra! De stunder då du ser de ungas egna vingar bära väger upp alla nödlandningar som slutat i stenig terräng.",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/erasmus-mobilitetsprojekt-ungdomsarbetare' target='_blank' rel='noopener noreferrer'>Erasmus+ mobilitetsprojekt för ungdomsarbetare</a>, <a href='https://www.oph.fi/sv/program/discovereu' target='_blank' rel='noopener noreferrer'>DiscoverEU</a>, <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank' rel='noopener noreferrer'>internationella utbildningar</a>.",
        'og_desc': "Du har varit med om mycket och har erfarenhet av internationell verksamhet. Gör testet!"
    },
    'rohkaisijakuoriainen': {
        'title': "Du är en Uppmuntrarbagge!",
        'desc': "Du ser till att alla känner sig hörda och sedda. Du är redo att hjälpa till i alla situationer. Du viskar uppmuntrande ord och känner till de vägar och möjligheter som ligger framför. Du ger dem omkring dig, både unga och kollegor, mod att bre ut sina vingar inför det nya!",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-solidaritetsprojekt' target='_blank' rel='noopener noreferrer'>Europeiska solidaritetskårens solidaritetsprojekt</a>, <a href='https://www.oph.fi/sv/program/erasmus-ungdomsverksamhet' target='_blank' rel='noopener noreferrer'>Erasmus+ ungdomsverksamhet</a> och <a href='https://www.oph.fi/sv/internationalisering/eurodesk' target='_blank' rel='noopener noreferrer'>Eurodesk-nätverket för ungdomsinformation</a>.",
        'og_desc': "Du ser till att alla känner sig hörda och sedda. Gör testet och ta reda på vilken karaktär du är!"
    },
    'osallisuuskimalainen': {
        'title': "Du är ett Delaktighetsbi!",
        'desc': "Du surrar av iver när unga hittar nya sätt att göra sin egen röst hörd. Du har tagit som din uppgift att se till att varje liten varelse i trädgården har sin egen plats i gruppen. Du vet vilka stödda rutter som erbjuds till världen, eller så tar du målmedvetet reda på det.",
        'info': "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-volontarverksamhet' target='_blank' rel='noopener noreferrer'>Europeiska solidaritetskårens volontärprojekt</a> och <a href='https://www.oph.fi/sv/program/erasmus-ungdomsutbyte' target='_blank' rel='noopener noreferrer'>Erasmus+ ungdomsutbyten</a>.",
        'og_desc': "Du surrar av iver när unga hittar nya sätt att göra sin egen röst hörd. Gör testet!"
    }
}

fi_data = {
    'unelmoijakorento': {
        'title': "Olet Unelmoijakorento!",
        'desc': "Silmäsi ovat avautuneet maailman vääryyksille ja haluat korjata sen, mikä on pielessä. Tunnistat pienen kokosi mutta et anna sen haitata muutoksesta unelmointia. Kokoonnut yhteen muiden kanssa, jotta äänenne olisi vahvempi. Maailman eriarvoisuus painaa siipiäsi, mutta toisaalta osaat kuvitella paremman tulevaisuuden.",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank' rel='noopener noreferrer'>Euroopan solidaarisuusjoukkojen solidaarisuushankkeet</a> ja <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank' rel='noopener noreferrer'>vapaaehtoishankkeet</a> sekä <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank' rel='noopener noreferrer'>kansainväliset koulutukset</a>.",
        'og_desc': "Silmäsi ovat avautuneet maailman vääryyksille. Tee testi ja selvitä oma hahmosi!"
    },
    'kehittajakehraaja': {
        'title': "Olet Kehittäjäkehrääjä!",
        'desc': "Tiedät, minne olet matkalla, vaikka et ole vielä nähnyt koko reittiä. Saat muutkin kokeilemaan asioita, jotka eivät vielä ole mahdollisia. Liidellessäsi kohti uusia verkostoja haaveilet käsitteistä ja menetelmistä, seminaareista, päättäjiin vaikuttamisesta ja eri näkökulmien törmäyttämisestä. Kehräät hankeideoita ratkaisuksi kohtaamiisi ongelmiin.",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-yhteistyohankkeet' target='_blank' rel='noopener noreferrer'>Erasmus+ yhteistyöhankkeet</a> ja <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank' rel='noopener noreferrer'>kansainväliset koulutukset</a>.",
        'og_desc': "Tiedät, minne olet matkalla. Tee testi ja selvitä oma hahmosi!"
    },
    'hallintomittari': {
        'title': "Olet Hallintomittari!",
        'desc': "Mittailet maailmaa omalta paikaltasi ja huomaat helposti, missä apuasi tarvitaan. Sujahdat ketterästi manuaalista raportointilomakkeelle. Oletkin tärkeä osanen populaatiosi toiminnassa, sillä ilman sinua eivät pyörät pyörisi tai ideat löytäisi maaliin saakka.",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-hakuajat-ja-neuvonnat' target='_blank' rel='noopener noreferrer'>Hakuneuvonnat Erasmus+ -hankkeille</a> ja <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukkojen-hakuajat-ja-neuvonnat' target='_blank' rel='noopener noreferrer'>Euroopan solidaarisuusjoukot -hankkeille</a>, <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank' rel='noopener noreferrer'>kansainväliset koulutukset</a>.",
        'og_desc': "Mittailet maailmaa omalta paikaltasi. Tee testi ja selvitä oma hahmosi!"
    },
    'seikkailijasirkka': {
        'title': "Olet Seikkailijasirkka!",
        'desc': "Olet ollut monessa mukana, ja sinulta löytyy kokemusta kansainvälisyydestä sekä ulkomailta että kotimaassa. Seikkailunnälkäsi ei kuitenkaan ole vielä taltutettu, vaan tutkit jo seuraavia mahdollisuuksia hypätä junaan ja löytää uusia maisemia, joissa siritellä yksin tai yhdessä muiden kanssa!",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisotyontekijoiden-liikkuvuushanke' target='_blank' rel='noopener noreferrer'>Erasmus+ nuorisotyöntekijöiden liikkuvuushankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/discovereu' target='_blank' rel='noopener noreferrer'>DiscoverEU</a>, <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank' rel='noopener noreferrer'>kansainväliset koulutukset</a>.",
        'og_desc': "Olet ollut monessa mukana ja sinulta löytyy kokemusta kansainvälisyydestä. Tee testi!"
    },
    'rohkaisijakuoriainen': {
        'title': "Olet Rohkaisijakuoriainen!",
        'desc': "Pidät huolen siitä, että jokaisella on kuultu ja nähty olo. Olet valmis auttamaan tilanteessa kuin tilanteessa. Supattelet rohkaisevia sanoja ja tunnet edessä olevat reitit ja mahdollisuudet. Annat ympärilläsi oleville, sekä nuorille että kollegoillesi, rohkeutta levittää siipensä uuden edessä!",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank' rel='noopener noreferrer'>Euroopan solidaarisuusjoukkojen solidaarisuushankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorten-osallistumishanke' target='_blank' rel='noopener noreferrer'>Erasmus+ nuorten osallistumishankeet</a>, <a href='https://www.oph.fi/fi/kansainvalisyys/eurodesk' target='_blank' rel='noopener noreferrer'>Eurodesk-nuorisotiedotusverkosto</a>.",
        'og_desc': "Pidät huolen siitä, että jokaisella on kuultu ja nähty olo. Tee testi ja selvitä oma hahmosi!"
    },
    'osallisuuskimalainen': {
        'title': "Olet Osallisuuskimalainen!",
        'desc': "Suriset innosta, kun nuoret löytävät uusia tapoja tuoda omaa ääntään kuuluviin. Olet ottanut asiaksesi varmistaa, että puutarhan jokaisella pienellä otuksella on oma paikkansa ryhmässä. Tiedät, minkälaisia tuettuja reittejä maailmalle on tarjolla, tai ainakin aiot ottaa siitä päättäväisesti selvää.",
        'info': "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank' rel='noopener noreferrer'>Euroopan solidaarisuusjoukkojen vapaaehtoishankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisovaihto' target='_blank' rel='noopener noreferrer'>Erasmus+ nuorisovaihdot</a>.",
        'og_desc': "Suriset innosta, kun nuoret löytävät uusia tapoja tuoda omaa ääntään kuuluviin. Tee testi!"
    }
}

template = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_description}">
    <meta property="og:image" content="https://kvseikkailijakysely.fi/assets/images/{char_key}.png">
    <link rel="stylesheet" href="../../css/style.css">
    <script src="https://cdn.counter.dev/script.js" data-id="4dd6d014-e826-4cda-8265-b742387017fc" data-utcoffset="2"></script>
</head>
<body class="result-page char-{char_key}">
    <div class="app-container">
        <div class="header-scene">
            <div class="scene-ui"></div>
            <div class="scene-bg">
                <div class="sun" id="sun"></div>
                <div class="layer layer-back" id="clouds"></div>
                <div class="layer layer-mid" id="mountains-back"></div>
                <div class="layer layer-front" id="mountains-mid"></div>
            </div>
            <div class="character-container result-mode">
                <img src="../../assets/images/{char_key}.png" class="character-img" alt="Character">
            </div>
        </div>
        <div class="content-area">
            <h2>{your_result_label}</h2>
            <h1>{title}</h1>
            <p>{desc}</p>
            
            <div class="share-section" style="margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 15px; text-align: center;">
                <p style="font-weight: bold; color: #006699; margin-bottom: 15px;">{share_label}</p>
                <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                    <a href="https://wa.me/?text={share_text}" target="_blank" class="btn" style="width: auto; padding: 10px 20px; font-size: 16px; background: #25D366; margin-bottom: 0;">WhatsApp</a>
                    <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank" class="btn" style="width: auto; padding: 10px 20px; font-size: 16px; background: #1877F2; margin-bottom: 0;">Facebook</a>
                    <button onclick="copyToClipboard()" class="btn" style="width: auto; padding: 10px 20px; font-size: 16px; background: #666; margin-bottom: 0;">{copy_link_label}</button>
                </div>
            </div>

            <div class="result-extra">
                <h3>{more_info_label}</h3>
                <p>{info}</p>
            </div>
            <a href="../../{lang}/index.html" class="btn">{take_test_label}</a>
            <div class="logo-grid">
                <img src="../../assets/images/{logo_edufi}" alt="EDUFI">
                <img src="../../assets/images/{logo_erasmus}" alt="Erasmus+">
                <img src="../../assets/images/{logo_esc}" alt="Solidarity Corps">
                <img src="../../assets/images/Eurodesk_Su_Ru_En.png" alt="Eurodesk">
            </div>
        </div>
        <footer style="padding: 20px; text-align: center; border-top: 1px solid #eee;">
            <a href="../../{privacy_link}" style="color: #666; text-decoration: none; font-size: 14px;">{privacy_label}</a> | 
            <a href="../../{accessibility_link}" style="color: #666; text-decoration: none; font-size: 14px;">{accessibility_label}</a>
        </footer>
    </div>
    <script>
        function copyToClipboard() {{
            var dummy = document.createElement("input");
            document.body.appendChild(dummy);
            dummy.value = window.location.href;
            dummy.select();
            document.execCommand("copy");
            document.body.removeChild(dummy);
            alert("{copy_success_label}");
        }}
    </script>
</body>
</html>"""

labels = {
    'fi': {
        'your_result_label': "Tuloksesi:",
        'more_info_label': "Lisätietoa:",
        'take_test_label': "Tee testi itse!",
        'privacy_label': "Tietosuojaseloste",
        'accessibility_label': "Saavutettavuusseloste",
        'og_title_template': "Olen {char_name}! Mikä seikkailija sinä olet?",
        'share_label': "Jaa tuloksesi somessa:",
        'copy_link_label': "Kopioi linkki",
        'copy_success_label': "Linkki kopioitu leikepöydälle!"
    },
    'en': {
        'your_result_label': "Your result:",
        'more_info_label': "More information:",
        'take_test_label': "Take the test yourself!",
        'privacy_label': "Privacy Policy",
        'accessibility_label': "Accessibility Statement",
        'og_title_template': "I am a {char_name}! Which adventurer are you?",
        'share_label': "Share your result:",
        'copy_link_label': "Copy Link",
        'copy_success_label': "Link copied to clipboard!"
    },
    'sv': {
        'your_result_label': "Ditt resultat:",
        'more_info_label': "Mer information:",
        'take_test_label': "Gör testet själv!",
        'privacy_label': "Integritetspolicy",
        'accessibility_label': "Tillgänglighetsutlåtande",
        'og_title_template': "Jag är en {char_name}! Vilken äventyrare är du?",
        'share_label': "Dela ditt resultat:",
        'copy_link_label': "Kopiera länk",
        'copy_success_label': "Länken har kopierats!"
    }
}

char_names_clean = {
    'fi': {
        'unelmoijakorento': "Unelmoijakorento",
        'kehittajakehraaja': "Kehittäjäkehrääjä",
        'hallintomittari': "Hallintomittari",
        'seikkailijasirkka': "Seikkailijasirkka",
        'rohkaisijakuoriainen': "Rohkaisijakuoriainen",
        'osallisuuskimalainen': "Osallisuuskimalainen"
    },
    'en': {
        'unelmoijakorento': "Dreamer Dragonfly",
        'kehittajakehraaja': "Developer Moth",
        'hallintomittari': "Coordinating Caterpillar",
        'seikkailijasirkka': "Adventure Cricket",
        'rohkaisijakuoriainen': "Encourager Beetle",
        'osallisuuskimalainen': "Participation Bee"
    },
    'sv': {
        'unelmoijakorento': "Drömmarslända",
        'kehittajakehraaja': "Idéspinnare",
        'hallintomittari': "Förvaltningsmätare",
        'seikkailijasirkka': "Äventyrssyrsa",
        'rohkaisijakuoriainen': "Uppmuntrarbagge",
        'osallisuuskimalainen': "Delaktighetsbi"
    }
}

for lang, data in [('fi', fi_data), ('en', en_data), ('sv', sv_data)]:
    if lang == 'en':
        logo_edufi = "OPH_En_vaaka_rgb.png"
        logo_erasmus = "Erasmus+_with_baseline-pos-ALL_lang_EN.png"
        logo_esc = "SolidarityCorps_without_tagline-EN.png"
    elif lang == 'sv':
        logo_edufi = "OPH_Su_Ru_vaaka_RGB.png"
        logo_erasmus = "Erasmus+_with_baseline-pos-ALL_lang_SV.png"
        logo_esc = "SolidarityCorps_without_tagline-SV.png"
    else: # fi
        logo_edufi = "OPH_Su_Ru_vaaka_RGB.png"
        logo_erasmus = "Erasmus+_left_with_baseline-pos-ALL_lang_FI.png"
        logo_esc = "Solidaarisuusjoukot.png"
    
    if lang == 'fi':
        privacy_link = "tietosuoja.html"
        accessibility_link = "fi/saavutettavuus.html"
    elif lang == 'en':
        privacy_link = "en/tietosuoja.html"
        accessibility_link = "en/saavutettavuus.html"
    elif lang == 'sv':
        privacy_link = "sv/tietosuoja.html"
        accessibility_link = "sv/saavutettavuus.html"
    
    for char_key, content in data.items():
        char_name = char_names_clean[lang][char_key]
        og_title = labels[lang]['og_title_template'].format(char_name=char_name)
        
        share_url = f"https://kvseikkailijakysely.fi/{lang}/tulokset/{char_key}.html"
        share_text = urllib.parse.quote(f"{og_title} {share_url}")
        
        file_content = template.format(
            lang=lang,
            title=content['title'],
            og_title=og_title,
            og_description=content['og_desc'],
            char_key=char_key,
            logo_edufi=logo_edufi,
            logo_erasmus=logo_erasmus,
            logo_esc=logo_esc,
            your_result_label=labels[lang]['your_result_label'],
            more_info_label=labels[lang]['more_info_label'],
            desc=content['desc'],
            info=content['info'],
            take_test_label=labels[lang]['take_test_label'],
            privacy_label=labels[lang]['privacy_label'],
            privacy_link=privacy_link,
            accessibility_label=labels[lang]['accessibility_label'],
            accessibility_link=accessibility_link,
            share_label=labels[lang]['share_label'],
            share_text=share_text,
            share_url=urllib.parse.quote(share_url),
            copy_link_label=labels[lang]['copy_link_label'],
            copy_success_label=labels[lang]['copy_success_label']
        )
        
        file_path = f"{lang}/tulokset/{char_key}.html"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

print(f"Generated {3 * len(fi_data)} files successfully.")
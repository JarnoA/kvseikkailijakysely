import os

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

labels = {
    'fi': {
        'your_result_label': "Tuloksesi:",
        'more_info_label': "Lisätietoa:",
        'restart_label': "Aloita alusta",
        'scan_label': "Skannaa QR-koodi ja ota tulos talteen!",
        'illustration_label': "Kuvitus: Minttu Nurmi",
        'privacy_label': "Tietosuojaseloste",
        'accessibility_label': "Saavutettavuusseloste",
        'og_title_template': "Olen {char_name}! Mikä seikkailija sinä olet?"
    },
    'en': {
        'your_result_label': "Your result:",
        'more_info_label': "More information:",
        'restart_label': "Start Over",
        'scan_label': "Scan the QR code to take the result with you!",
        'illustration_label': "Illustration by: Minttu Nurmi",
        'privacy_label': "Privacy Policy",
        'accessibility_label': "Accessibility Statement",
        'og_title_template': "I am a {char_name}! Which adventurer are you?"
    },
    'sv': {
        'your_result_label': "Ditt resultat:",
        'more_info_label': "Mer information:",
        'restart_label': "Börja om",
        'scan_label': "Skanna QR-koden och spara ditt resultat!",
        'illustration_label': "Bild: Minttu Nurmi",
        'privacy_label': "Integritetspolicy",
        'accessibility_label': "Tillgänglighetsutlåtande",
        'og_title_template': "Jag är en {char_name}! Vilken äventyrare är du?"
    }
}

template_fair = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_description}">
    <meta property="og:image" content="https://kvseikkailijakysely.fi/assets/images/{char_key}.png">
    <link rel="stylesheet" href="../../../css/style.css">
    <script src="https://cdn.counter.dev/script.js" data-id="4dd6d014-e826-4cda-8265-b742387017fc" data-utcoffset="2"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
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
                <img src="../../../assets/images/{char_key}.png" class="character-img" alt="Character">
            </div>
        </div>
        <div class="content-area">
            <h2>{your_result_label}</h2>
            <h1>{title}</h1>
            <p>{desc}</p>
            <p class="illustration-credit">{illustration_label}</p>
            
            <div class="qr-section" style="text-align: center; margin: 10px 0 30px 0; padding: 20px; background: rgba(255,255,255,0.5); border-radius: 15px;">
                <p style="margin-bottom: 15px; font-weight: bold; color: #006699;">{scan_label}</p>
                <div id="qr-code-container" style="display: flex; justify-content: center;"></div>
                <p style="margin-top: 15px; font-size: 14px;"><a href="https://kvseikkailijakysely.fi/{lang}/tulokset/{char_key}.html" style="color: #006699;">kvseikkailijakysely.fi/{lang}/tulokset/{char_key}.html</a></p>
            </div>

            <div class="result-extra">
                <h3>{more_info_label}</h3>
                <p>{info}</p>
            </div>

            <a href="../../index.html" class="btn">{restart_label}</a>
            
            <div class="logo-grid">
                <img src="../../../assets/images/{logo_edufi}" alt="EDUFI">
                <img src="../../../assets/images/{logo_erasmus}" alt="Erasmus+">
                <img src="../../../assets/images/{logo_esc}" alt="Solidarity Corps">
                <img src="../../../assets/images/Eurodesk_Su_Ru_En.png" alt="Eurodesk">
            </div>
        </div>
        <footer style="padding: 20px; text-align: center; border-top: 1px solid #eee;">
            <a href="../../../{privacy_link}" style="color: #666; text-decoration: none; font-size: 14px;">{privacy_label}</a> | 
            <a href="../../../{accessibility_link}" style="color: #666; text-decoration: none; font-size: 14px;">{accessibility_label}</a>
        </footer>
    </div>
    <script>
        window.onload = function() {{
            var resultUrl = "https://kvseikkailijakysely.fi/{lang}/tulokset/{char_key}.html";
            new QRCode(document.getElementById("qr-code-container"), {{
                text: resultUrl,
                width: 160,
                height: 160,
                colorDark : "#006699",
                colorLight : "#ffffff",
                correctLevel : 2 // H level
            }});
        }};
    </script>
</body>
</html>"""

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
        
        file_content = template_fair.format(
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
            restart_label=labels[lang]['restart_label'],
            scan_label=labels[lang]['scan_label'],
            illustration_label=labels[lang]['illustration_label'],
            privacy_label=labels[lang]['privacy_label'],
            privacy_link=privacy_link,
            accessibility_label=labels[lang]['accessibility_label'],
            accessibility_link=accessibility_link
        )
        
        # Fair path
        file_path = f"{lang}/tulokset/fair/{char_key}.html"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

print(f"Generated {3 * len(fi_data)} FAIR files successfully.")
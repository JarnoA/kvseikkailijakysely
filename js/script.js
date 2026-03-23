const quizData = {
    fi: {
        characters: {
            'unelmoijakorento': {
                title: "Olet Unelmoijakorento!",
                desc: "Silmäsi ovat avautuneet maailman vääryyksille ja haluat korjata sen, mikä on pielessä. Tunnistat pienen kokosi mutta et anna sen haitata muutoksesta unelmointia. Kokoonnut yhteen muiden kanssa, jotta äänenne olisi vahvempi. Maailman eriarvoisuus painaa siipiäsi, mutta toisaalta osaat kuvitella paremman tulevaisuuden.",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank'>Euroopan solidaarisuusjoukkojen solidaarisuushankkeet</a> ja <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank'>vapaaehtoishankkeet</a> sekä <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank'>kansainväliset koulutukset</a>.",
                image: "../assets/images/unelmoijakorento.png",
                rank: 1
            },
            'kehittajakehraaja': {
                title: "Olet Kehittäjäkehrääjä!",
                desc: "Tiedät, minne olet matkalla, vaikka et ole vielä nähnyt koko reittiä. Saat muutkin kokeilemaan asioita, jotka eivät vielä ole mahdollisia. Liidellessäsi kohti uusia verkostoja haaveilet käsitteistä ja menetelmistä, seminaareista, päättäjiin vaikuttamisesta ja eri näkökulmien törmäyttämisestä. Kehräät hankeideoita ratkaisuksi kohtaamiisi ongelmiin.",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-yhteistyohankkeet' target='_blank'>Erasmus+ yhteistyöhankkeet</a> ja <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank'>kansainväliset koulutukset</a>.",
                image: "../assets/images/kehittajakehraaja.png",
                rank: 2
            },
            'hallintomittari': {
                title: "Olet Hallintomittari!",
                desc: "Mittailet maailmaa omalta paikaltasi ja huomaat helposti, missä apuasi tarvitaan. Lennähdät elegantisti manuaalista raportointilomakkeelle. Oletkin tärkeä osanen populaatiosi toiminnassa, sillä ilman sinua eivät pyörät pyörisi tai ideat löytäisi maaliin saakka.",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-hakuajat-ja-neuvonnat' target='_blank'>Hakuneuvonnat Erasmus+ -hankkeille</a> ja <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukkojen-hakuajat-ja-neuvonnat' target='_blank'>Euroopan solidaarisuusjoukot -hankkeille</a>, <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank'>kansainväliset koulutukset</a>.",
                image: "../assets/images/hallintomittari.png",
                rank: 3
            },
            'seikkailijasirkka': {
                title: "Olet Seikkailijasirkka!",
                desc: "Olet ollut monessa mukana, ja sinulta löytyy kokemusta kansainvälisyydestä sekä ulkomailta että kotimaassa. Seikkailunnälkäsi ei kuitenkaan ole vielä taltutettu, vaan tutkit jo seuraavia mahdollisuuksia hypätä junaan ja löytää uusia maisemia, joissa siritellä yksin tai yhdessä muiden kanssa!",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuisotyontekijoiden-liikkuvuushanke' target='_blank'>Erasmus+ nuorisotyöntekijöiden liikkuvuushankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/discovereu' target='_blank'>DiscoverEU</a>, <a href='https://www.oph.fi/fi/ohjelmat/kansainvaliset-koulutukset-nuorisoalan-toimijoille' target='_blank'>kansainväliset koulutukset</a>.",
                image: "../assets/images/seikkailijasirkka.png",
                rank: 4
            },
            'rohkaisijakuoriainen': {
                title: "Olet Rohkaisijakuoriainen!",
                desc: "Pidät huolen siitä, että jokaisella on kuultu ja nähty olo. Olet valmis auttamaan tilanteessa kuin tilanteessa. Supattelet rohkaisevia sanoja ja tunnet edessä olevat reitit ja mahdollisuudet. Annat ympärilläsi oleville, sekä nuorille että kollegoillesi, rohkeutta levittää siipensä uuden edessä!",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank'>Euroopan solidaarisuusjoukkojen solidaarisuushankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorten-osallistumishanke' target='_blank'>Erasmus+ nuorten osallistumishankeet</a>, <a href='https://www.oph.fi/fi/kansainvalisyys/eurodesk' target='_blank'>Eurodesk-nuorisotiedotusverkosto</a>.",
                image: "../assets/images/rohkaisijakuoriainen.png",
                rank: 5
            },
            'osallisuuskimalainen': {
                title: "Olet Osallisuuskimalainen!",
                desc: "Suriset innosta, kun nuoret löytävät uusia tapoja tuoda omaa ääntään kuuluviin. Olet ottanut asiaksesi varmistaa, että puutarhan jokaisella pienellä otuksella on oma paikkansa ryhmässä. Tiedät, minkälaisia tuettuja reittejä maailmalle on tarjolla, tai ainakin aiot ottaa siitä päättäväisesti selvää.",
                info: "Tutustu ainakin näihin: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank'>Euroopan solidaarisuusjoukkojen vapaaehtoishankkeet</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisovaihto' target='_blank'>Erasmus+ nuorisovaihdot</a>.",
                image: "../assets/images/osallisuuskimalainen.png",
                rank: 6
            }
        },
        questions: [
            { text: "Kaupunki suunnittelee muutoksia nuorten palveluihin. Miten reagoit?", options: [
                { text: "Osallistun mielenosoitukseen tai muuhun näkyvään vaikuttamiseen.", scores: { 'unelmoijakorento': 3, 'osallisuuskimalainen': 3 } },
                { text: "Laadin kirjallisen hakemuksen, kannanoton tai palautteen päättäjille.", scores: { 'kehittajakehraaja': 3, 'hallintomittari': 3 } },
                { text: "Toimin kentällä nuorten kanssa ja organisoin toimintaa heidän kanssaan.", scores: { 'seikkailijasirkka': 3 } },
                { text: "Keskityn ensin kuuntelemaan muiden ajatuksia ja kokemuksia asiasta.", scores: { 'rohkaisijakuoriainen': 3 } }
            ]},
            { text: "Mikä näistä on sinulle mieluisinta tekemistä?", options: [
                { text: "Nähdä, miten toinen uskaltaa tehdä jotakin uutta.", scores: { 'rohkaisijakuoriainen': 2, 'osallisuuskimalainen': 2 } },
                { text: "Tallata uuden kaupungin katuja yhdessä muiden kanssa.", scores: { 'seikkailijasirkka': 2, 'unelmoijakorento': 2 } },
                { text: "Ratkaista oikean elämän ongelma sujuvalla excelöinnillä.", scores: { 'hallintomittari': 2 } },
                { text: "Jakaa tuoreiden tuttavuuksien kanssa ideoita ja kokemuksia.", scores: { 'kehittajakehraaja': 2 } }
            ]},
            { text: "Olette tekemässä yhteistä projektia pienessä ryhmässä. Mikä rooli sopii sinulle parhaiten?", options: [
                { text: "Olen taustavaikuttaja, joka hoitaa oman osa-alueensa.", scores: { 'hallintomittari': 2 } },
                { text: "Olen tukiroolissa: osallistun mutten johda.", scores: { 'kehittajakehraaja': 2, 'rohkaisijakuoriainen': 2 } },
                { text: "Olen aktiivinen osallistuja, joka tuo uusia ideoita ja vie tehtäviä eteenpäin.", scores: { 'unelmoijakorento': 2, 'osallisuuskimalainen': 2 } },
                { text: "Olen projektin moottori, joka ohjaa kokonaisuutta ja organisoi tekemistä.", scores: { 'seikkailijasirkka': 2 } }
            ]},
            { text: "Ovatko Erasmus+ nuorisoalalle ja Euroopan solidaarisuusjoukot jo tuttuja?", options: [
                { text: "Täysin vieraat", scores: { 'unelmoijakorento': 1 } },
                { text: "Melko vieraat", scores: { 'hallintomittari': 1 } },
                { text: "Melko tutut", scores: { 'osallisuuskimalainen': 1, 'rohkaisijakuoriainen': 1 } },
                { text: "Täysin tutut", scores: { 'seikkailijasirkka': 1, 'kehittajakehraaja': 1 } }
            ]},
            { text: "Mikä on mottosi?", options: [
                { text: "Hätä keinot keksii.", scores: { 'osallisuuskimalainen': 1, 'seikkailijasirkka': 1 } },
                { text: "Kaveria ei jätetä.", scores: { 'rohkaisijakuoriainen': 1 } },
                { text: "Hyvin suunniteltu on puoliksi tehty.", scores: { 'hallintomittari': 1 } },
                { text: "Aamu on iltaa viisaampi.", scores: { 'unelmoijakorento': 1, 'kehittajakehraaja': 1 } }
            ]}
        ]
    },
    en: {
        characters: {
            'unelmoijakorento': {
                title: "You are a Dreamer Dragonfly!",
                desc: "Your eyes have been opened to the wrongs of the world and you want to put right what's wrong. You are aware of your small size but don't let it get in the way of dreaming of change. You gather together with others to make your voice stronger. You're weighed down by inequality in the world, but you can also imagine a better future.",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank'>The European Solidarity Corps’ solidarity projects (in Finnish)</a> and <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank'>volunteer projects (in Finnish)</a> as well as <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank'>international training</a>.",
                image: "../assets/images/unelmoijakorento.png",
                rank: 1
            },
            'kehittajakehraaja': {
                title: "You are a Developer Moth!",
                desc: "You know where you're headed, even if you haven't seen the whole route yet. You have a way of also getting others to try things that are not yet possible. As you flutter towards new networks, you dream about concepts and methods, seminars, influencing decision-makers and bringing different perspectives together. You turn project ideas into solutions to the problems that you face.",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-yhteistyohankkeet' target='_blank'>Erasmus+ partnerships for cooperation (in Finnish)</a> and <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank'>international training</a>.",
                image: "../assets/images/kehittajakehraaja.png",
                rank: 2
            },
            'hallintomittari': {
                title: "You are a Coordinating Caterpillar!",
                desc: "You measure the world from where you are and can easily spot where your help is needed. You spring elegantly from manual to reporting form. You’re an important part of your population’s activities, as without you the wheels wouldn't turn or the ideas wouldn't reach the finish line.",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisoalalle-hakuajat-ja-neuvonnat' target='_blank'>Briefings for Erasmus+ projects (in Finnish)</a> and <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukkojen-hakuajat-ja-neuvonnat' target='_blank'>European Solidarity Corps projects (in Finnish)</a>, <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank'>international training</a>.",
                image: "../assets/images/hallintomittari.png",
                rank: 3
            },
            'seikkailijasirkka': {
                title: "You are an Adventure Cricket!",
                desc: "You've been involved in many things and have international experience, both abroad and at home. But your thirst for adventure hasn’t been sated yet, which is why you're already exploring the next opportunities to hop on a train and discover new landscapes to explore alone or with others! The moments when you see young people's own wings carrying them make up for all the emergency landings on the rocks.",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisotyontekijoiden-liikkuvuushanke' target='_blank'>Erasmus+ mobility of youth workers (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/discovereu' target='_blank'>DiscoverEU (in Finnish)</a>, <a href='https://www.oph.fi/en/education-development-and-internationalisation/erasmus-programme-finland-2021-2027/international-training-youth-sector' target='_blank'>international training</a>.",
                image: "../assets/images/seikkailijasirkka.png",
                rank: 4
            },
            'rohkaisijakuoriainen': {
                title: "You are an Encourager Beetle!",
                desc: "You make sure that everyone feels heard and seen. You are ready to help others in every situation. You shower people with words of encouragement and know the paths and opportunities ahead. You give those around you, both young people and your colleagues, the courage to spread their wings in the face of new things!",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-solidaarisuushanke' target='_blank'>European Solidarity Corps’ solidarity projects (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorten-osallistumishanke' target='_blank'>Erasmus+ youth participation activities (in Finnish)</a>, <a href='https://www.oph.fi/en/internationalisation/eurodesk' target='_blank'>Eurodesk youth information network</a>.",
                image: "../assets/images/rohkaisijakuoriainen.png",
                rank: 5
            },
            'osallisuuskimalainen': {
                title: "You are a Participation Bee!",
                desc: "You're inspired by young people finding new ways to make their voices heard. You've made it your business to make sure that every little creature in the garden has its place in the group. You know what kind of supported routes to the world are available, or at least you're determined to find out about them.",
                info: "Check out at least the following: <a href='https://www.oph.fi/fi/ohjelmat/euroopan-solidaarisuusjoukot-vapaaehtoistoiminta' target='_blank'>European Solidarity Corps’ volunteer projects (in Finnish)</a>, <a href='https://www.oph.fi/fi/ohjelmat/erasmus-nuorisovaihto' target='_blank'>Erasmus+ youth exchanges (in Finnish)</a>.",
                image: "../assets/images/osallisuuskimalainen.png",
                rank: 6
            }
        },
        questions: [
            { text: "Your home city is planning changes to its youth services. How do you react?", options: [
                { text: "I take part in a demonstration or other visible influence activities.", scores: { 'unelmoijakorento': 3, 'osallisuuskimalainen': 3 } },
                { text: "I submit a written application, comment or feedback to the decision-makers.", scores: { 'kehittajakehraaja': 3, 'hallintomittari': 3 } },
                { text: "I work in the field with young people and organise activities with them.", scores: { 'seikkailijasirkka': 3 } },
                { text: "I focus first on listening to other people's thoughts and experiences about the issue.", scores: { 'rohkaisijakuoriainen': 3 } }
            ]},
            { text: "Which of these is your favourite thing to do?", options: [
                { text: "Seeing someone else have the courage to do something new.", scores: { 'rohkaisijakuoriainen': 2, 'osallisuuskimalainen': 2 } },
                { text: "Stomping the streets of a new city with others.", scores: { 'seikkailijasirkka': 2, 'unelmoijakorento': 2 } },
                { text: "Solving a real-life problem with functional spreadsheets.", scores: { 'hallintomittari': 2 } },
                { text: "Sharing ideas and experiences with new acquaintances to create something completely new.", scores: { 'kehittajakehraaja': 2 } }
            ]},
            { text: "You are working on a joint project in a small group. Which of the following roles suits you best?", options: [
                { text: "I'm in the background, only working on my own part of the project.", scores: { 'hallintomittari': 2 } },
                { text: "I'm in a supporting role, participating but not leading.", scores: { 'kehittajakehraaja': 2, 'rohkaisijakuoriainen': 2 } },
                { text: "I’m an active participant, bringing new ideas and working on tasks.", scores: { 'unelmoijakorento': 2, 'osallisuuskimalainen': 2 } },
                { text: "I’m the engine of the project, guiding the whole and organising the work.", scores: { 'seikkailijasirkka': 2 } }
            ]},
            { text: "Are you already familiar with Erasmus+ Youth and the European Solidarity Corps?", options: [
                { text: "Completely unfamiliar", scores: { 'unelmoijakorento': 1 } },
                { text: "Quite unfamiliar", scores: { 'hallintomittari': 1 } },
                { text: "Quite familiar", scores: { 'osallisuuskimalainen': 1, 'rohkaisijakuoriainen': 1 } },
                { text: "Completely familiar", scores: { 'seikkailijasirkka': 1, 'kehittajakehraaja': 1 } }
            ]},
            { text: "What is your motto?", options: [
                { text: "Where there’s a will, there’s a way.", scores: { 'osallisuuskimalainen': 1, 'seikkailijasirkka': 1 } },
                { text: "No one gets left behind.", scores: { 'rohkaisijakuoriainen': 1 } },
                { text: "Well begun is half done.", scores: { 'hallintomittari': 1 } },
                { text: "The morning is wiser than the evening.", scores: { 'unelmoijakorento': 1, 'kehittajakehraaja': 1 } }
            ]}
        ]
    },
    sv: {
        characters: {
            'unelmoijakorento': {
                title: "Du är en Drömmarslända!",
                desc: "Dina ögon har öppnats för orättvisorna i världen, och du vill rätta till det som är fel. Du är medveten om din litenhet, men låter den inte hindra dig från att drömma om förändring. Du samlas med andra för att göra er röst starkare. Världens ojämlikhet tynger dina vingar, men samtidigt har du förmågan att föreställa dig en bättre framtid.",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-solidaritetsprojekt' target='_blank'>Europeiska solidaritetskårens solidaritetsprojekt</a> och <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-volontarverksamhet' target='_blank'>volontärprojekt</a> samt <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank'>internationella utbildningar</a>.",
                image: "../assets/images/unelmoijakorento.png",
                rank: 1
            },
            'kehittajakehraaja': {
                title: "Du är en Idéspinnare!",
                desc: "Du vet vart du är på väg, även om du ännu inte ser hela vägen. Du får också andra att pröva på sådant som ännu inte är möjligt. När du rör dig mot nya nätverk drömmer du om begrepp och metoder, seminarier, påverkan på beslutsfattare och om att föra samman olika perspektiv. Du spinner vidare projektidéer till lösningar på de problem du möter.",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/erasmus-ungdomssektorn-partnerskap-samarbete' target='_blank'>Erasmus+ partnerskap för samarbete</a> och <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank'>internationella utbildningar</a>.",
                image: "../assets/images/kehittajakehraaja.png",
                rank: 2
            },
            'hallintomittari': {
                title: "Du är en Förvaltningsmätare!",
                desc: "Du mäter världen från din egen plats och ser snabbt var din insats behövs. Du rör dig smidigt från manualer till rapporteringsblanketter. Du är en viktig del av helheten, för utan dig skulle hjulen inte snurra och idéerna inte nå hela vägen fram.",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/ansokningstiderna-och-radgivning-ansokan' target='_blank'>Ansökningsrådgivningar för Erasmus+-projekt</a> ja <a href='https://www.oph.fi/sv/program/ansokningstider-och-radgivningar-europeiska-solidaritetskaren' target='_blank'>projekt inom Europeiska solidaritetskåren</a>, <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank'>internationella utbildningar</a>.",
                image: "../assets/images/hallintomittari.png",
                rank: 3
            },
            'seikkailijasirkka': {
                title: "Du är en Äventyrssyrsa!",
                desc: "Du har varit med om mycket och har erfarenhet av internationella sammanhang både utomlands och i Finland. Din äventyrslust är dock fortfarande inte stillad – du utforskar redan nya möjligheter att hoppa på tåget och upptäcka nya miljöer där du kan spela ensam eller tillsammans med andra! De stunder då du ser de ungas egna vingar bära väger upp alla nödlandningar som slutat i stenig terräng.",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/discovereu' target='_blank'>DiscoverEU</a>, <a href='https://www.oph.fi/sv/program/erasmus-mobilitetsprojekt-ungdomsarbetare' target='_blank'>Erasmus+ mobilitetsprojekt för ungdomsarbetare</a> och <a href='https://www.oph.fi/sv/program/internationella-utbildningar-aktorer-pa-ungdomsomradet' target='_blank'>internationella utbildningar</a>.",
                image: "../assets/images/seikkailijasirkka.png",
                rank: 4
            },
            'rohkaisijakuoriainen': {
                title: "Du är en Uppmuntrarbagge!",
                desc: "Du ser till att alla känner sig hörda och sedda. Du är redo att hjälpa till i alla situationer. Du viskar uppmuntrande ord och känner till de vägar och möjligheter som ligger framför. Du ger dem omkring dig, både unga och kollegor, mod att bre ut sina vingar inför det nya!",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/internationalisering/eurodesk' target='_blank'>Eurodesk-nätverket för ungdomsinformation</a>, <a href='https://www.oph.fi/sv/program/erasmus-ungdomsverksamhet' target='_blank'>Erasmus+ ungdomsverksamhet</a> ja <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-solidaritetsprojekt' target='_blank'>Europeiska solidaritetskårens solidaritetsprojekt</a>.",
                image: "../assets/images/rohkaisijakuoriainen.png",
                rank: 5
            },
            'osallisuuskimalainen': {
                title: "Du är ett Delaktighetsbi!",
                desc: "Du surrar av iver när unga hittar nya sätt att göra sin egen röst hörd. Du har tagit som din uppgift att se till att varje liten varelse i trädgården har sin egen plats i gruppen. Du vet vilka stödda rutter som erbjuds till världen, eller så tar du målmedvetet reda på det.",
                info: "Ta gärna del av följande: <a href='https://www.oph.fi/sv/program/europeiska-solidaritetskaren-volontarverksamhet' target='_blank'>Europeiska solidaritetskårens volontärprojekt</a> och <a href='https://www.oph.fi/sv/program/erasmus-ungdomsutbyte' target='_blank'>Erasmus+ ungdomsutbyten</a>.",
                image: "../assets/images/osallisuuskimalainen.png",
                rank: 6
            }
        },
        questions: [
            { text: "Staden planerar ändringar i tjänsterna för unga. Hur reagerar du?", options: [
                { text: "Jag deltar i en demonstration eller annan synlig påverkan.", scores: { 'unelmoijakorento': 3, 'osallisuuskimalainen': 3 } },
                { text: "Jag skriver en skriftlig ansökan, ett ställningstagande eller respons till beslutsfattarna.", scores: { 'kehittajakehraaja': 3, 'hallintomittari': 3 } },
                { text: "Jag arbetar ute på fältet med unga och organiserar verksamhet tillsammans med dem.", scores: { 'seikkailijasirkka': 3 } },
                { text: "Jag börjar med att lyssna på andras tankar och erfarenheter i frågan.", scores: { 'rohkaisijakuoriainen': 3 } }
            ]},
            { text: "Vilket av följande tycker du mest om att göra?", options: [
                { text: "Att se hur någon vågar göra något nytt.", scores: { 'rohkaisijakuoriainen': 2, 'osallisuuskimalainen': 2 } },
                { text: "Att vandra på gatorna i en ny stad tillsammans med andra.", scores: { 'seikkailijasirkka': 2, 'unelmoijakorento': 2 } },
                { text: "Att lösa ett verkligt problem med hjälp av smidig excel-användning.", scores: { 'hallintomittari': 2 } },
                { text: "Att dela idéer ja erfarenheter med nya bekantskaper för att skapa något helt nytt.", scores: { 'kehittajakehraaja': 2 } }
            ]},
            { text: "Ni arbetar med ett gemensamt projekt i en liten grupp. Vilken roll passar dig bäst?", options: [
                { text: "Jag är en bakgrundspåverkare som sköter mitt eget delområde.", scores: { 'hallintomittari': 2 } },
                { text: "Jag har en stödjande roll: jag deltar men leder inte.", scores: { 'kehittajakehraaja': 2, 'rohkaisijakuoriainen': 2 } },
                { text: "Jag är en aktiv deltagare som bidrar med nya idéer och driver uppgifterna framåt.", scores: { 'unelmoijakorento': 2, 'osallisuuskimalainen': 2 } },
                { text: "Jag är projektets motor som leder helheten och organiserar arbetet.", scores: { 'seikkailijasirkka': 2 } }
            ]},
            { text: "Är Erasmus+ för ungdomssektorn och Europeiska solidaritetskåren redan bekanta program för dig?", options: [
                { text: "Helt obekanta", scores: { 'unelmoijakorento': 1 } },
                { text: "Ganska obekanta", scores: { 'hallintomittari': 1 } },
                { text: "Ganska bekanta", scores: { 'osallisuuskimalainen': 1, 'rohkaisijakuoriainen': 1 } },
                { text: "Helt bekanta", scores: { 'seikkailijasirkka': 1, 'kehittajakehraaja': 1 } }
            ]},
            { text: "Vad är ditt motto?", options: [
                { text: "Nöden är uppfinningarnas moder.", scores: { 'osallisuuskimalainen': 1, 'seikkailijasirkka': 1 } },
                { text: "Man överger inte en kamrat.", scores: { 'rohkaisijakuoriainen': 1 } },
                { text: "Välplanerat är hälften gjort.", scores: { 'hallintomittari': 1 } },
                { text: "Det är bäst att sova på saken.", scores: { 'unelmoijakorento': 1, 'kehittajakehraaja': 1 } }
            ]}
        ]
    }
};

const app = {
    state: {
        lang: 'fi',
        currentStep: 0,
        scores: { 'unelmoijakorento': 0, 'kehittajakehraaja': 0, 'hallintomittari': 0, 'seikkailijasirkka': 0, 'rohkaisijakuoriainen': 0, 'osallisuuskimalainen': 0 }
    },

    init: function() {
        const path = window.location.pathname;
        if (path.includes('/en/')) this.state.lang = 'en';
        else if (path.includes('/sv/')) this.state.lang = 'sv';
        else this.state.lang = 'fi';
        
        console.log("App Initialized. Language:", this.state.lang);
    },

    startQuiz: function() {
        this.resetScores();
        this.state.currentStep = 0;
        
        document.body.classList.remove('result-page');
        const charContainer = document.getElementById('avatar-container');
        if (charContainer) charContainer.classList.remove('result-mode');

        this.switchView('view-question');
        this.renderQuestion();
    },

    resetScores: function() {
        for (let key in this.state.scores) this.state.scores[key] = 0;
    },

    renderQuestion: function() {
        const data = quizData[this.state.lang] || quizData['fi'];
        const questions = data.questions;
        const q = questions[this.state.currentStep];
        const total = questions.length;
        
        document.getElementById('question-text').innerText = q.text;
        const stageLabel = (this.state.lang === 'en') ? 'Stage' : (this.state.lang === 'sv' ? 'Etapp' : 'Etappi');
        document.getElementById('question-counter').innerText = `${stageLabel} ${this.state.currentStep + 1} / ${total}`;
        
        const percent = ((this.state.currentStep) / total) * 100;
        document.getElementById('progress-fill').style.width = percent + '%';

        const charContainer = document.getElementById('avatar-container');
        const sun = document.getElementById('sun');
        const clouds = document.getElementById('clouds');
        const mountBack = document.getElementById('mountains-back');
        const mountMid = document.getElementById('mountains-mid');

        let charPos = 15 + (this.state.currentStep * 15); 
        let cloudPos = this.state.currentStep * 30;
        let mountBackPos = this.state.currentStep * -40; 
        let mountMidPos = this.state.currentStep * -100; 
        let sunPos = this.state.currentStep * 60; 

        if (charContainer) charContainer.style.left = charPos + '%';
        if (sun) sun.style.transform = `translateX(${sunPos}px)`;
        if (clouds) clouds.style.transform = `translateX(${cloudPos}px)`;
        if (mountBack) mountBack.style.transform = `translateX(${mountBackPos}px)`;
        if (mountMid) mountMid.style.transform = `translateX(${mountMidPos}px)`;

        if (charContainer) {
            charContainer.classList.remove('bounce');
            void charContainer.offsetWidth; 
            charContainer.classList.add('bounce');
            
            // Antennae animation
            const antL = document.getElementById('antenna-l');
            const antR = document.getElementById('antenna-r');
            if (antL && antR) {
                const angle = (this.state.currentStep % 2 === 0) ? 0 : -20;
                antL.style.transform = `rotate(${angle}deg)`;
                antR.style.transform = `rotate(${-angle}deg)`;
            }
        }

        const container = document.getElementById('options-container');
        container.innerHTML = ''; 

        q.options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'btn btn-outline fade-in';
            btn.innerText = opt.text;
            btn.onclick = () => this.handleAnswer(opt.scores);
            container.appendChild(btn);
        });
    },

    handleAnswer: function(scoresToAdd) {
        for (let char in scoresToAdd) {
            if (this.state.scores[char] !== undefined) this.state.scores[char] += scoresToAdd[char];
        }
        this.state.currentStep++;
        const total = quizData[this.state.lang].questions.length;
        if (this.state.currentStep < total) {
             document.getElementById('progress-fill').style.width = (this.state.currentStep / total) * 100 + '%';
             setTimeout(() => { this.renderQuestion(); }, 200);
        } else {
            this.finishQuiz();
        }
    },

    finishQuiz: function() {
        document.getElementById('progress-fill').style.width = '100%';
        const winnerKey = this.calculateWinner();
        this.showResult(winnerKey);
    },

    calculateWinner: function() {
        const scores = this.state.scores;
        let maxScore = -1;
        let winners = [];
        for (let char in scores) {
            if (scores[char] > maxScore) { maxScore = scores[char]; winners = [char]; }
            else if (scores[char] === maxScore) winners.push(char);
        }
        if (winners.length === 1) return winners[0];
        
        // Rule 2: Override Rule
        if (winners.includes('unelmoijakorento') && winners.includes('osallisuuskimalainen')) return 'osallisuuskimalainen';
        
        // Rule 1: Fixed Ranking
        winners.sort((a, b) => quizData['fi'].characters[a].rank - quizData['fi'].characters[b].rank);
        return winners[0];
    },

    showResult: function(charKey) {
        // Clear any previous character classes
        const classesToRemove = Array.from(document.body.classList).filter(c => c.startsWith('char-'));
        classesToRemove.forEach(c => document.body.classList.remove(c));
        
        document.body.classList.add('result-page', 'char-' + charKey);
        const data = quizData[this.state.lang] || quizData['fi'];
        const charData = data.characters[charKey];
        if (!charData) return;

        document.getElementById('result-title').innerText = charData.title;
        document.getElementById('result-desc').innerText = charData.desc;
        
        const illuLabel = (this.state.lang === 'en') ? 'Illustration by:' : (this.state.lang === 'sv' ? 'Bild:' : 'Kuvitus:');
        const illuEl = document.getElementById('result-illustration');
        if (illuEl) illuEl.innerText = `${illuLabel} Minttu Nurmi`;
        
        document.getElementById('result-info').innerHTML = charData.info;
        
        const charContainer = document.getElementById('avatar-container');
        if (charContainer) {
            charContainer.classList.add('result-mode');
            
            // Show character PNG and hide bunny SVG
            const svgBunny = document.getElementById('avatar-svg');
            if (svgBunny) svgBunny.style.display = 'none';
            
            let charImg = document.getElementById('char-result-img');
            if (!charImg) {
                charImg = document.createElement('img');
                charImg.id = 'char-result-img';
                charImg.className = 'character-img';
                charContainer.appendChild(charImg);
            }
            charImg.src = charData.image;
            charImg.style.display = 'block';
        }

        // Virtual page view for analytics
        try {
            window.location.hash = 'tulos-' + charKey;
        } catch (e) {
            console.warn("Analytics hash failed:", e);
        }
        
        try {
            const qrContainer = document.getElementById('qr-code-container');
            if (qrContainer && typeof QRCode !== 'undefined') {
                qrContainer.innerHTML = ''; 
                const resultUrl = `https://kvseikkailijakysely.fi/${this.state.lang}/tulokset/${charKey}.html`;
                new QRCode(qrContainer, {
                    text: resultUrl, width: 160, height: 160,
                    colorDark : "#006699", colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                });
            }
        } catch (e) { console.error("QR fail", e); }

        this.switchView('view-result');
    },

    restart: function() {
        const rootPath = window.location.pathname.split('tulokset/')[0];
        window.location.href = rootPath;
    },

    switchView: function(viewId) {
        document.querySelectorAll('.view').forEach(el => { 
            el.classList.remove('active'); 
            el.style.display = 'none'; 
            el.style.paddingTop = '0px'; // Reset any runtime padding
        });
        const target = document.getElementById(viewId);
        if (target) { target.classList.add('active'); target.style.display = 'block'; }
    }
};

app.init();
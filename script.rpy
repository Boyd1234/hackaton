################################################################################
## NEXIO & CO - Cybersecurity Choose Your Own Adventure
## Jij bent de nieuwe CSO van NeXio & Co (800 werknemers)
################################################################################

################################################################################
## 1. Assets & Schalen
################################################################################
image bg office          = im.Scale("bg office.png", 1920, 1080)
image bg office_night    = im.Scale("bg office_night.jpg", 1920, 1080)
image bg boardroom       = im.Scale("bg boardroom.jpg", 1920, 1080)
image bg server_room     = im.Scale("bg server_room.jpg", 1920, 1080)
image bg hack_attack     = im.Scale("bg hack_attack.jpg", 1920, 1080)
image bg news_flash      = im.Scale("bg news_flash.jpg", 1920, 1080)
image bg lobby           = im.Scale("bg lobby.jpg", 1920, 1080)
image bg ceo_office      = im.Scale("bg ceo_office.jpg", 1920, 1080)
image bg parking         = im.Scale("bg parking.jpg", 1920, 1080)

image sarah   = im.FactorScale("sarah.png", 1.8)
image mark    = im.FactorScale("mark.png", 1.8)
image ceo     = im.FactorScale("ceo.png", 1.8)
image werknemer = im.FactorScale("werknemer.png", 1.8)

################################################################################
## 2. Variabelen & Dashboard
################################################################################
default bedrijfsnaam    = "NeXio & Co"
default budget          = 750000
default reputatie       = 100
default security_waarde = 0
default datalek         = False

# Leningen
default lening          = 0
default aantal_leningen = 0
default max_leningen    = 2

# Wachtwoord-minigame
default wachtwoorden_gelijk = False
default dom_wachtwoord      = False
default ww_database         = ""
default ww_admin            = ""

# Vlaggen voor eindevaluatie
default heeft_mfa           = False
default open_googledrive     = False
default auto_blokkering      = False
default developer_admin      = False
default updates_genegeerd    = False
default onveilige_iot        = False
default byod_risico          = False
default ceo_laptop_verloren  = False
default onveilige_wifi       = False
default sketchy_software     = False
default pen_test_gedaan      = False
default phishing_gebeten     = False

define s    = Character("Sarah (IT Consultant)", image="sarah",    color="#3498db")
define m    = Character("Mark (CFO)",             image="mark",     color="#e67e22")
define ceo_c = Character("CEO",                   image="ceo",      color="#9b59b6")
define w    = Character("Lisa (Werknemer)",        image="werknemer",color="#27ae60")
define news = Character("NIEUWS",                              color="#e74c3c")
define mail = Character("E-MAILBOX",                           color="#ecf0f1")
define sys  = Character("SYSTEEM",                             color="#f1c40f")

################################################################################
## 3. Status Overlay
################################################################################
screen status_overlay():
    zorder 100
    frame:
        xalign 0.98
        yalign 0.02
        background Solid("#1a252fdd")
        padding (18, 12)
        vbox:
            spacing 6
            text "[ NeXio & Co ]" size 16 bold True color "#3498db"
            hbox:
                spacing 8
                text "BUDGET:"    size 16 color "#bdc3c7"
                text "€ [budget:,d]" size 18 bold True color "#2ecc71"
            hbox:
                spacing 8
                text "REPUTATIE:" size 16 color "#bdc3c7"
                text "[reputatie]%" size 18 bold True color "#f39c12"
            hbox:
                spacing 8
                text "SECURITY:"  size 16 color "#bdc3c7"
                text "[security_waarde] pts" size 18 bold True color "#3498db"
            if lening > 0:
                hbox:
                    spacing 8
                    text "SCHULD:"    size 16 color "#e74c3c"
                    text "€ [lening:,d]" size 18 bold True color "#e74c3c"

################################################################################
## HULPFUNCTIE: lening pop-up
################################################################################
screen lening_popup(bedrag, rente):
    modal True
    zorder 200
    frame:
        xalign 0.5
        yalign 0.4
        background Solid("#1a252fee")
        padding (30, 20)
        vbox:
            spacing 12
            text "⚠ ONVOLDOENDE BUDGET" size 22 bold True color "#e74c3c"
            text "De bank biedt een noodlening aan:" size 18 color "#ecf0f1"
            text "€ [bedrag:,d]  (terugbetalen: € [rente:,d])" size 18 color "#f39c12"
            hbox:
                spacing 20
                textbutton "Accepteer lening" action Return(True)  style "button"
                textbutton "Weiger"           action Return(False) style "button"

################################################################################
## 4. INTRODUCTIE
################################################################################
label start:
    scene black
    show screen status_overlay

    "[ WELKOM BIJ NEXIO & CO ]"
    "Het jaar is 2024. NeXio & Co is een snelgroeiend technologiebedrijf met 800 werknemers."
    "Na een reeks kleine beveiligingsincidenten heeft de Raad van Bestuur besloten: er komt een nieuwe Chief Security Officer."
    "Dat ben jij."
    "Je takenpakket? Alle grote securitybeslissingen voor het komende kwartaal doorvoeren."
    "Je start met een budget van €750.000. Elke euro die je uitgeeft, is er één minder voor je bonus."
    "Maar bezuinig je te hard? Dan betaal je later een véél hogere prijs."
    "Aan het einde van het kwartaal probeert een hackersgroep het bedrijf binnen te dringen. Jouw keuzes bepalen wat er dan gebeurt."

    scene bg boardroom with fade
    show sarah at left  with dissolve
    show mark  at right with dissolve
    show werknemer at center with dissolve

    s "Goedemorgen! Ik ben Sarah, uw IT-consultant voor dit kwartaal. Ik zal u door alle beveiligingsbeslissingen loodsen."
    m "Mark, CFO. Eén verzoek: houd de kosten in toom. We zijn geen bank."
    w "Lisa, ik vertegenwoordig de 800 werknemers. Wat u ook beslist – denk aan ons."

    jump deel1_identiteit

################################################################################
## 5. DEEL 1: Identiteit & Toegang
################################################################################
label deel1_identiteit:
    scene bg boardroom with dissolve
    show sarah at left
    show mark  at right

    "[ DEEL 1 — IDENTITEIT & TOEGANG ]"
    s "We beginnen met het fundament: wie mag wat doen binnen onze systemen?"

    ## --- 5A: MFA ---
label menu_mfa:
    s "Punt één: Two-Factor Authentication (2FA/MFA). Op dit moment logt iedereen in met alleen een wachtwoord."
    m "Kost dat iets?"
    s "Enterprise MFA-platform: €55.000 eenmalig. Alternatief: gratis Google Authenticator, maar dan handmatig uitrollen. Dat kost maanden werk en mensen gaan het omzeilen."

    menu:
        "Koop Enterprise MFA-platform (-€55.000)":
            if budget - 55000 < 0:
                jump lening_mfa
            $ budget -= 55000
            $ security_waarde += 40
            $ heeft_mfa = True
            s "Uitstekend. Elke medewerker logt nu in met wachtwoord + telefoon. Zelfs een gelekt wachtwoord is nutteloos voor aanvallers."
            m "Duur, maar ik snap het."
        
        "Verplicht gratis Google Authenticator (+€0, maar reputatieverlies)":
            $ reputatie -= 10
            $ security_waarde += 20
            $ heeft_mfa = True
            s "Het werkt, maar de uitrol duurt twee maanden en 30% van de medewerkers gaat het 'tijdelijk' overslaan. Risico blijft."
            w "Ik vind het heel omslachtig eerlijk gezegd..."
        
        "MFA overslaan, wachtwoorden zijn voldoende (+€0)":
            $ security_waarde -= 20
            s "Dat is een serieus risico. Elke phishing-aanval die een wachtwoord buitmaakt, geeft direct toegang tot het systeem."
            m "Maar het kost niks. Lekker."

    ## --- 5B: Wachtwoorden ---
label menu_wachtwoorden:
    s "Punt twee: wachtwoordbeleid. We moeten wachtwoorden instellen voor de Klantendatabase en het Admin-paneel."
    m "Ik hoor mensen nu al zuchten als ik 'wachtwoord' zeg."

    menu:
        "Koop Password Manager licenties voor alle medewerkers (-€35.000)":
            if budget - 35000 < 0:
                jump lening_wachtwoord
            $ budget -= 35000
            $ security_waarde += 35
            s "Perfect. Unieke, complexe wachtwoorden per dienst. Niemand hoeft meer iets te onthouden of op te schrijven."
            w "Oh, dat is eigenlijk wel handig!"
        
        "Verplicht wachtwoord wijzigen elke 3 maanden (-€8.000)":
            $ budget -= 8000
            $ security_waarde += 5
            $ reputatie -= 15
            s "Dit werkt averechts. Mensen gaan 'Nexio2024!' veranderen in 'Nexio2025!'. Schijnveiligheid."
            m "Maar we voldoen aan de regelgeving. Mooi."
            w "Ik haat dit al. Echt."
        
        "Zelf twee master-wachtwoorden verzinnen (+€0)":
            s "Oke... wat wordt het wachtwoord voor de KLANTENDATABASE?"
            $ ww_database = renpy.input("Typ wachtwoord Klantendatabase:").strip()
            s "En voor het ADMIN-PANEEL?"
            $ ww_admin = renpy.input("Typ wachtwoord Admin-paneel:").strip()

            if ww_database == ww_admin:
                $ wachtwoorden_gelijk = True
                $ security_waarde -= 50
                s "BEIDE wachtwoorden zijn '[ww_database]'?! Als één lek is, is ALLES lek. Dit is een ramp in wording."
                m "Gemakkelijk te onthouden! Efficiënt!"
            elif ww_database.lower() in ["admin", "1234", "password", "nexio", "welkom", "123456"] or ww_admin.lower() in ["admin", "1234", "password", "nexio", "welkom", "123456"]:
                $ dom_wachtwoord = True
                $ security_waarde -= 40
                s "Echt?! '[ww_database]' en '[ww_admin]'? Een script raadt dit in seconden."
            else:
                $ security_waarde -= 10
                s "Ze zijn tenminste verschillend. Maar gedeelde wachtwoorden blijven kwetsbaar. Zet het nergens op!"

    ## --- 5C: Open Google Drive ---
label menu_googledrive:
    s "Punt drie: onze gedeelde mappen. Op dit moment staat de Google Drive van de marketingafdeling op 'Openbaar toegankelijk'. Iedereen met de link kan alles zien."
    m "Maar zo werken we makkelijk samen met externe partners!"

    menu:
        "Sluit de Drive, implementeer toegangsbeleid (-€15.000 voor training)":
            $ budget -= 15000
            $ security_waarde += 25
            s "Slim. Alleen geautoriseerde medewerkers en goedgekeurde partners krijgen nu toegang."
        
        "Laat het open, maar zet er een waarschuwing bij (+€0)":
            $ open_googledrive = True
            $ security_waarde -= 15
            s "Een waarschuwing helpt niet. Gevoelige klantdata staat gewoon open op het internet."
            m "Niemand weet toch hoe ze dat moeten vinden?"
            s "Mark... Google kan dat indexeren."

    ## --- 5D: Ontslagen werknemer ---
label menu_ontslagen_werknemer:
    scene bg ceo_office with dissolve
    show ceo_c at center with dissolve
    show sarah at left

    s "Belangrijk: volgende week wordt een senior medewerker ontslagen wegens wangedrag. Die persoon heeft nu nog toegang tot alle systemen, klantdata en de mailserver."
    ceo_c "Kunnen we die toegang niet gewoon handmatig intrekken na het gesprek?"
    s "Dat duurt minstens 48 uur via IT. Er bestaat geautomatiseerde software die het bij ontslag direct afsluit."

    menu:
        "Koop automated offboarding software (-€28.000)":
            if budget - 28000 < 0:
                jump lening_offboarding
            $ budget -= 28000
            $ security_waarde += 30
            $ auto_blokkering = True
            s "Uitstekend. Op het moment dat HR op 'bevestigen' drukt, zijn alle accounts geblokkeerd. Geen kans op wraakactie."
        
        "Handmatig regelen via IT, duurt 48 uur (+€0)":
            $ security_waarde -= 20
            $ reputatie -= 5
            s "48 uur is lang. Een ontevreden ex-werknemer kan in die tijd veel schade aanrichten of data doorspelen aan concurrenten."
            m "We hebben toch vertrouwen in onze mensen?"
            s "Tot we dat niet meer hebben, ja."

    ## --- 5E: Developer admin-rechten ---
label menu_developer_admin:
    scene bg boardroom with dissolve
    show sarah at left
    show mark  at right

    s "Laatste punt in dit blok: de developers klagen. Ze willen admin-rechten op de productieomgeving zodat ze niet steeds IT hoeven te vragen."
    m "Ze zijn toch al de hele dag aan het wachten. Geef ze gewoon die rechten."

    menu:
        "Geef developers volledige admin-rechten (+€0, snel)":
            $ developer_admin = True
            $ security_waarde -= 25
            $ reputatie += 5
            s "Als één developer-account gehackt wordt, heeft de aanvaller nu admin-toegang tot alles. Principe van 'least privilege' is hier volledig losgelaten."
        
        "Implementeer Privileged Access Management (-€40.000)":
            if budget - 40000 < 0:
                jump lening_pam
            $ budget -= 40000
            $ security_waarde += 35
            s "Goed. Developers krijgen tijdelijke verhoogde rechten via een PAM-systeem met logging. Flexibel én veilig."
        
        "Weiger, procedures blijven zoals ze zijn (+€0)":
            $ reputatie -= 10
            $ security_waarde += 10
            s "Veilig, maar de developers zijn woedend. Productiviteit daalt. Sommigen gaan 'creatieve' omwegen zoeken."
            w "Ik heb al iemand horen zeggen dat ze gewoon lokaal gaan werken..."

    jump deel2_endpoints

################################################################################
## Lening-tussenscenes Deel 1
################################################################################
label lening_mfa:
    m "Budget is ontoereikend. De bank biedt €80.000 aan (terugbetalen: €96.000)."
    menu:
        "Accepteer lening":
            $ aantal_leningen += 1
            $ budget += 80000
            $ lening += 96000
        "Weiger, sla MFA over":
            $ security_waarde -= 20
            s "Dat begrijp ik niet, maar oké."
    jump menu_mfa

label lening_wachtwoord:
    m "Budget is ontoereikend. De bank biedt €50.000 aan (terugbetalen: €60.000)."
    menu:
        "Accepteer lening":
            $ aantal_leningen += 1
            $ budget += 50000
            $ lening += 60000
        "Weiger, gebruik zelf verzinnen":
            pass
    jump menu_wachtwoorden

label lening_offboarding:
    m "Budget te laag. Lening van €40.000 (terugbetalen: €48.000)?"
    menu:
        "Accepteer lening":
            $ aantal_leningen += 1
            $ budget += 40000
            $ lening += 48000
        "Weiger":
            $ security_waarde -= 20
            s "Dan doen we het handmatig. 48 uur risico."
    jump menu_ontslagen_werknemer

label lening_pam:
    m "Budget te laag. Lening van €55.000 (terugbetalen: €66.000)?"
    menu:
        "Accepteer lening":
            $ aantal_leningen += 1
            $ budget += 55000
            $ lening += 66000
        "Weiger":
            pass
    jump menu_developer_admin

################################################################################
## 6. DEEL 2: Apparaten & Endpoints
################################################################################
label deel2_endpoints:
    scene bg office with fade
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[ DEEL 2 — APPARATEN & ENDPOINTS ]"
    s "Goed, we gaan naar de apparaten. Endpoints zijn de voordeur van elke aanval."

    ## --- 6A: Updates ---
label menu_updates:
    s "Onze systemen draaien deels op software met bekende kritieke beveiligingslekken. Er is een grote update-campagne nodig: alle 800 machines."
    m "Dat betekent downtime. Werknemers klagen altijd over die verplichte herstarts."

    menu:
        "Automatisch patchbeheer invoeren (-€20.000)":
            if budget - 20000 < 0:
                m "Budget te laag."
                $ updates_genegeerd = True
                jump menu_iot
            $ budget -= 20000
            $ security_waarde += 30
            s "Alle systemen worden buiten werktijden automatisch bijgewerkt. Geen downtime, geen excuses."
        
        "Eenmalige handmatige update-campagne (-€5.000)":
            $ budget -= 5000
            $ security_waarde += 10
            s "Beter dan niks, maar over zes maanden staan we opnieuw achter."
        
        "Updates uitstellen tot na het kwartaal (+€0)":
            $ updates_genegeerd = True
            $ security_waarde -= 30
            s "Dit is hoe 90% van de succesvolle hacks beginnen. Bekende lekken, niet gepatcht."
            m "Maar iedereen is productief! Geen gemopperde herstarts!"

    ## --- 6B: Onveilige IoT ---
label menu_iot:
    s "We hebben 45 IP-camera's en smart thermostaten in het gebouw. Ze draaien allemaal op de standaard fabriekswachtwoorden."
    m "Ze werken toch? Camera's laten licht knipperen, thermostaat regelt temperatuur..."

    menu:
        "Isoleer IoT op apart netwerksegment + wijzig wachtwoorden (-€18.000)":
            if budget - 18000 < 0:
                m "Budget te laag, overslaan."
                $ onveilige_iot = True
                jump menu_byod
            $ budget -= 18000
            $ security_waarde += 25
            $ onveilige_iot = False
            s "Goed. Zelfs als een camera gehackt wordt, kan de aanvaller niet bij onze servers."
        
        "Alleen wachtwoorden wijzigen (-€3.000)":
            $ budget -= 3000
            $ security_waarde += 10
            s "Beter, maar ze zitten nog steeds op hetzelfde netwerk als de servers. Niet ideaal."
        
        "Laat alles zoals het is (+€0)":
            $ onveilige_iot = True
            $ security_waarde -= 20
            s "IP-camera's zijn een favoriete toegangspoort voor aanvallers. Ze zijn krachtig, altijd aan, en niemand let erop."

    ## --- 6C: BYOD (eigen laptop) ---
label menu_byod:
    show werknemer at center with dissolve
    w "Eh... ik wilde vragen: mijn werkcomputer doet raar. Mag ik tijdelijk mijn privé-laptop gebruiken?"
    s "Dit is precies het vraagstuk: Bring Your Own Device. Privé-laptops hebben mogelijk geen antivirusupdates, kunnen geïnfecteerd zijn, en verbinden straks met ons netwerk."

    menu:
        "Nee, lever een tijdelijke leencomputer uit (-€500 per geval, geregeld in beleid -€10.000)":
            $ budget -= 10000
            $ security_waarde += 20
            w "Oh, dat is eerlijk eigenlijk."
            s "Goed beleid. Geen onbekende apparaten op ons netwerk."
        
        "Ja, maar alleen via VPN en op een apart gastnetwerk (+€0)":
            $ byod_risico = False
            $ security_waarde += 5
            s "Redelijk compromis. Niet perfect, maar geïsoleerd."
            w "Top, dankjewel!"
        
        "Ja, gewoon op het normale netwerk (+€0, snel)":
            $ byod_risico = True
            $ security_waarde -= 25
            s "Als die laptop een keylogger heeft, lezen aanvallers straks alles wat getypt wordt op ons netwerk."
            m "Ze kunnen toch gewoon voorzichtig zijn?"

    ## --- 6D: CEO-laptop verloren ---
label menu_ceo_laptop:
    hide werknemer
    scene bg parking with dissolve
    show ceo_c at center with dissolve
    show sarah at left

    ceo_c "Sarah... ik heb mijn laptop in de trein laten liggen. Ik had er gisteren nog klantcontracten op staan."
    s "Is de schijf versleuteld? Is er een remote-wipe ingesteld?"

    menu:
        "We hadden full-disk encryptie + remote wipe ingesteld (-€0, als het er was)":
            if security_waarde >= 30:
                $ security_waarde += 10
                s "Dan is er geen probleem. De data is onleesbaar zonder de sleutel."
                ceo_c "Gelukkig. Lessen geleerd."
            else:
                s "Maar dat hadden we NIET ingesteld. De data staat nu open op een verloren apparaat."
                $ reputatie -= 20
                $ security_waarde -= 20
                $ datalek = True
        
        "We hadden niets ingesteld... (reputatieschade)":
            $ reputatie -= 25
            $ security_waarde -= 25
            $ datalek = True
            s "Dit is een datalek. We zijn verplicht dit te melden bij de Autoriteit Persoonsgegevens. Dat wordt nieuws."
            m "Mijn aandelenopties zijn nu waardeloos..."

    jump deel3_infrastructuur

################################################################################
## 7. DEEL 3: IT-omgeving & Infrastructuur
################################################################################
label deel3_infrastructuur:
    scene bg server_room with dissolve
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[ DEEL 3 — IT-OMGEVING & INFRASTRUCTUUR ]"
    s "Nu de infrastructuurlaag. Hier zitten de echte schaakstukken."

    ## --- 7A: Wifi ---
label menu_wifi:
    s "Het bedrijfsnetwerk heeft één wifi-netwerk: medewerkers, bezoekers en servers zitten er allemaal op."
    m "We hebben toch een wachtwoord erop? 'NeXio2019'. Staat op elk vergaderscherm."

    menu:
        "Netwerksegmentatie: apart gastnet, medewerkers-net, server-net (-€25.000)":
            if budget - 25000 < 0:
                m "Budget te laag, overslaan."
                $ onveilige_wifi = True
                jump menu_firewall
            $ budget -= 25000
            $ security_waarde += 30
            $ onveilige_wifi = False
            s "Ideaal. Een bezoeker die malware meebrengt kan nooit bij onze productiesystemen."
        
        "Alleen het wifi-wachtwoord aanpassen (+€0)":
            $ onveilige_wifi = True
            $ security_waarde -= 5
            s "Betere hygiene, maar iedereen zit nog steeds op hetzelfde netwerk."
        
        "Laat alles zoals het is (+€0)":
            $ onveilige_wifi = True
            $ security_waarde -= 25
            s "'NeXio2019' staat op elk vergaderscherm. Een bezoeker kan met vijf minuten werk ons volledige netwerk scannen."

    ## --- 7B: Firewall & monitoring ---
label menu_firewall:
    s "We hebben een basisrouter met ingebouwde firewall. Geen intrusion detection, geen logging, geen alerts."
    m "Die router doet zijn werk al tien jaar. Wat wil je meer?"

    menu:
        "Next-Gen Firewall + SIEM monitoring (-€80.000/jaar)":
            if budget - 80000 < 0:
                jump lening_firewall
            $ budget -= 80000
            $ security_waarde += 50
            s "Nu kunnen we aanvallen in real-time detecteren en automatisch blokkeren. Dit is de gouden standaard."
        
        "Basis firewall-upgrade (-€15.000)":
            $ budget -= 15000
            $ security_waarde += 20
            s "Beter. Maar we missen detection-mogelijkheden. Als ze eenmaal binnen zijn, merken we het te laat."
        
        "Niets doen (+€0)":
            $ security_waarde -= 30
            s "Een aanvaller kan wekenlang rondlopen in ons netwerk zonder dat we het weten. Gemiddeld duurt het 200 dagen voor een lek ontdekt wordt."
            m "200 dagen?! Dat meen je niet..."
            s "Helaas wel."

    jump deel4_applicaties

label lening_firewall:
    m "Budget te laag. Lening van €100.000 (terugbetalen: €120.000)?"
    menu:
        "Accepteer":
            $ aantal_leningen += 1
            $ budget += 100000
            $ lening += 120000
        "Weiger, neem basis-upgrade":
            $ budget -= 15000
            $ security_waarde += 20
            s "Basis-upgrade het is dan."
            jump deel4_applicaties
    jump menu_firewall

################################################################################
## 8. DEEL 4: Applicaties & Data
################################################################################
label deel4_applicaties:
    scene bg office with dissolve
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[ DEEL 4 — APPLICATIES & DATA ]"
    s "Bijna klaar met de preventieve maatregelen. Dan nu de applicatielaag."

    ## --- 8A: Sketchy software ---
label menu_sketchy_software:
    s "De financiële afdeling wil een software-pakket voor rapportage. Er is een gratis 'cracked' versie online, of we betalen €12.000 voor de licentie."
    m "Gratis is toch gratis? Het is exact dezelfde software!"
    w "Ik heb die gratis versie zelf ook al gebruikt thuis..."

    menu:
        "Koop officiële licentie (-€12.000)":
            $ budget -= 12000
            $ security_waarde += 15
            s "Verstandig. Geen verborgen malware, support inbegrepen, updates automatisch."
        
        "Download de gratis cracked versie (+€0)":
            $ sketchy_software = True
            $ security_waarde -= 35
            s "Cracked software is een van de meest gebruikte methodes om malware te verspreiden. We installeren potentieel een backdoor op 40 werkstations."
            m "Maar het bespaart €12.000!"

    ## --- 8B: Pentesting ---
label menu_pentest:
    s "We lanceren volgende maand een nieuwe klanten-webapplicatie. Wil je externe ethische hackers inhuren om die te testen voor we live gaan?"
    m "Wachten op hackers die ons BETAALD aanvallen? Dat klinkt achterlijk."
    s "Het heet een penetratietest. Ze zoeken lekken zodat echte hackers ze niet als eerste vinden."

    menu:
        "Ja, externe pentest inhuren (-€45.000)":
            if budget - 45000 < 0:
                m "Budget te laag, overslaan."
                $ pen_test_gedaan = False
                jump deel5_phishing
            $ budget -= 45000
            $ security_waarde += 40
            $ pen_test_gedaan = True
            s "Uitstekend. Ze vonden drie kritieke kwetsbaarheden. Allemaal gedicht voor de lancering."
            m "Oké, dat was achteraf toch de moeite waard."
        
        "Nee, intern team doet een snelle check (+€0)":
            $ pen_test_gedaan = False
            $ security_waarde += 5
            s "Intern team mist de tools en ervaring. We missen waarschijnlijk complexe kwetsbaarheden."
        
        "Nee, we lanceren gewoon (+€0)":
            $ pen_test_gedaan = False
            $ security_waarde -= 20
            s "Een ongeteste applicatie in productie. Elke scriptkiddie kan die scannen op dag één."

    jump deel5_phishing

################################################################################
## 9. DEEL 5: De Phishing Mail (CEO Fraud)
################################################################################
label deel5_phishing:
    scene bg ceo_office with dissolve
    show ceo_c at center with dissolve

    "[ DEEL 5 — MENSELIJKE FOUTEN ]"
    "Een donderdagmiddag. De CEO zit alleen in zijn kantoor. Er komt een e-mail binnen met HOGE PRIORITEIT."

    mail "VAN: sarah.itconsultant.nexio@gmai1.com\nAAN: ceo@nexio-co.com\nONDERWERP: URGENT: Server licenties verlopen VANDAAG!"
    mail "Beste,\n\nIk zit vast in een noodvergadering met een leverancier en mijn bank-app blokkeert internationale betalingen."
    mail "De factuur voor onze kritieke cloudomgeving moet VOOR 17:00 betaald zijn. Anders gaan alle servers offline en verliezen we alle klantdata van het kwartaal!"
    mail "Kun jij direct €22.500 overmaken naar:\nNL99 SCAM 0123 4567 89\n\nAlvast veel dank!\nSarah\n— Verstuurd via iPhone"

    menu:
        "Maak direct €22.500 over om downtime te voorkomen (-€22.500)":
            if budget - 22500 < 0:
                "De transactie mislukt wegens onvoldoende saldo. Je bent ongelooflijk gelukkig geweest."
            else:
                $ budget -= 22500
                $ reputatie -= 20
                $ phishing_gebeten = True
                "Je maakt het geld over."
                show sarah at left with dissolve
                s "Eh... CSO? Ik heb u vandaag helemaal geen mail gestuurd. Ik zit hier gewoon aan mijn bureau."
                "Je maag draait om. CEO Fraude. Het geld is weg. De daders zijn onvindbaar."

        "Stuur naar spam en negeer (+€0)":
            $ security_waarde += 5
            "Je verwijdert de mail zonder verdere actie."
            show sarah at left with dissolve
            s "Goed gedaan! Kijk: het e-mailadres is 'gmai1.com' — met een cijfer 1 in plaats van een L. Klassieke truc."

        "Bel Sarah direct om te verifiëren (+€0, beste optie)":
            $ security_waarde += 20
            show sarah at left with dissolve
            s "Hallo? Mail? Nee hoor, ik heb u niks gestuurd. Dit is een Whaling-aanval (CEO Fraud). Zet het adres in quarantaine!"
            s "Dit is precies waarom we nooit mogen handelen onder kunstmatige tijdsdruk. Altijd verifiëren via een ander kanaal."

        "Betaal en stuur tegelijk een waarschuwing naar IT (+€0)":
            $ budget -= 22500
            $ reputatie -= 10
            $ phishing_gebeten = True
            $ security_waarde -= 10
            show sarah at left with dissolve
            s "U heeft al betaald... De waarschuwing is te laat. En die rekening is nep."

    jump de_aanval

################################################################################
## 10. DE HACK — De Finale
################################################################################
label de_aanval:
    scene bg server_room with pixellate
    "[ KWARTAAL EINDIGT — DE AANVAL BEGINT ]"
    "Drie maanden later. Midden in de nacht gaat uw telefoon."

    ## Zwaarste scenario: zelfde wachtwoord
    if wachtwoorden_gelijk:
        with hpunch
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        show sarah at left
        s "CSO!! CRISIS! Een medewerker is gephisht en zijn database-wachtwoord '[ww_database]' is uitgelekt!"
        s "Omdat u voor het Admin-paneel EXACT HETZELFDE wachtwoord had gebruikt, hebben de hackers nu volledige controle over alle systemen van [bedrijfsnaam]!"
        s "Ze versleutelen alles. RANSOMWARE. Alles ligt plat."
        $ datalek = True
        $ budget -= 500000
        $ reputatie -= 95

    elif dom_wachtwoord:
        with hpunch
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        show sarah at left
        s "Een brute-force script raadde het admin-wachtwoord '[ww_admin]' in drie seconden. Ze zijn volledig binnen."
        $ datalek = True
        $ budget -= 300000
        $ reputatie -= 70

    else:
        ## Bereken aanvalkracht op basis van specifieke zwakheden
        $ aanval_kracht = renpy.random.randint(30, 70)

        ## Bonus aanvalskracht per zwakheid
        if sketchy_software:
            $ aanval_kracht += 20
        if onveilige_iot:
            $ aanval_kracht += 15
        if updates_genegeerd:
            $ aanval_kracht += 15
        if byod_risico:
            $ aanval_kracht += 10
        if onveilige_wifi:
            $ aanval_kracht += 10
        if developer_admin:
            $ aanval_kracht += 10
        if open_googledrive:
            $ aanval_kracht += 10
        if phishing_gebeten:
            $ aanval_kracht += 15
        if not heeft_mfa:
            $ aanval_kracht += 10

        if security_waarde >= aanval_kracht:
            show sarah at left with dissolve
            s "CSO! We worden aangevallen — maar onze systemen houden stand!"
            if pen_test_gedaan:
                s "De kwetsbaarheden die we bij de pentest vonden en dichtten... ze probeerden er exact doorheen te komen. Goed dat we dat hadden gedaan."
            if heeft_mfa:
                s "MFA blokkeerde meerdere gecompromitteerde wachtwoorden automatisch."
            $ reputatie += 10
            if reputatie > 100:
                $ reputatie = 100
        else:
            with hpunch
            scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
            show sarah at left

            if sketchy_software:
                s "De backdoor in de cracked software gaf ze al drie weken onopgemerkte toegang..."
                $ budget -= 200000
                $ datalek = True
                $ reputatie -= 50
            elif onveilige_iot:
                s "Ze kwamen binnen via een IP-camera met het standaard wachtwoord 'admin'. Vandaar konden ze het hele netwerk bereiken."
                $ budget -= 150000
                $ datalek = True
                $ reputatie -= 40
            elif updates_genegeerd:
                s "Ze gebruikten een patch die al 4 maanden beschikbaar was maar die wij nooit hadden geïnstalleerd."
                $ budget -= 120000
                $ reputatie -= 35
            else:
                s "Ze zijn via een zwak punt binnengedrongen. Alles ligt plat. Klantdata is buitgemaakt."
                $ budget -= 100000
                $ datalek = True
                $ reputatie -= 30

    jump eindscherm

################################################################################
## 11. EINDSCHERM
################################################################################
label eindscherm:
    hide screen status_overlay
    scene bg news_flash with dissolve

    "[ HET OORDEEL VAN DE RAAD VAN BESTUUR ]"
    ""
    "Eindbudget:    € [budget:,d]"
    if lening > 0:
        "Uitstaande schuld: € [lening:,d]"
    "Publieke reputatie: [reputatie]%"
    "Security score: [security_waarde] punten"

    if wachtwoorden_gelijk:
        news "BREAKING: Hackers wandelen bij [bedrijfsnaam] naar binnen dankzij hergebruikt wachtwoord '[ww_admin]'. CSO ontslagen."
        "U bent direct ontslagen. Het incident staat in alle vakbladen als schoolvoorbeeld van wat niet moet."
    elif datalek and reputatie < 20:
        news "BREAKING: Massaal datalek bij [bedrijfsnaam]. Klanten klagen bedrijf aan. Aandelenkoers keldert 60%."
        "U bent op staande voet ontslagen. Het herstel kost het bedrijf miljoenen."
    elif datalek:
        news "BREAKING: Hack bij [bedrijfsnaam] legt systemen plat. Klantdata gestolen."
        "U bent ontslagen wegens nalatigheid. De aanval had voorkomen kunnen worden."
    elif lening > budget:
        "U heeft de hack weerstaan — maar de schulden overtreffen de kas. [bedrijfsnaam] is technisch failliet."
        "Een pyrrusoverwinning."
    elif reputatie < 40:
        "De hack is voorkomen, maar uw harde bezuinigingen en slechte communicatie hebben de reputatie vernietigd."
        "Het personeel staakt. Klanten vertrekken. U treedt af."
    elif reputatie < 70:
        "Een gemengd resultaat. De aanval is deels weerstaan maar er is schade. De Raad houdt u onder toezicht."
        "Volgende kwartaal moeten de cijfers beter."
    elif security_waarde >= 150:
        "PERFECTE SCORE. U heeft [bedrijfsnaam] omgetoverd tot een fortress. De aanval stuitte op een muur."
        "U wordt geroemd als de beste CSO in de sector. Uw budget is intact en de reputatie onbeschadigd."
        news "NeXio & Co weerhoudt massale cyberaanval: 'We waren klaar.'"
    else:
        "U heeft de aanval overleefd. Budget intact, reputatie solide, medewerkers tevreden."
        "De Raad verlengt uw contract voor twee jaar. Goed gedaan, CSO."

    "[ EINDE — Start opnieuw voor een andere aanpak ]"
    return

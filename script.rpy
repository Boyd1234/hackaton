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
default budget          = 2500000
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
define news = Character("NIEUWS",                                  color="#e74c3c")
define mail = Character("E-MAILBOX",                               color="#ecf0f1")
define sys  = Character("SYSTEEM",                                 color="#f1c40f")

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
            text "[[ NeXio & Co ]" size 16 bold True color "#3498db"
            hbox:
                spacing 8
                text "BUDGET:"    size 16 color "#bdc3c7"
                text "€ [budget:,d]" size 18 bold True color "#2ecc71"
            hbox:
                spacing 8
                text "REPUTATIE:" size 16 color "#bdc3c7"
                text "[reputatie]%%" size 18 bold True color "#f39c12"
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
## 4. INTRODUCTIE
################################################################################
label start:
    scene black
    show screen status_overlay

    "[[ WELKOM BIJ NEXIO & CO ]"
    "Het jaar is 2024. NeXio & Co is een snelgroeiend technologiebedrijf met 800 werknemers."
    "Na een reeks kleine beveiligingsincidenten heeft de Raad van Bestuur besloten: er komt een nieuwe Chief Security Officer."
    "Dat ben jij."
    "Je takenpakket? Alle grote enterprise securitybeslissingen voor het komende kwartaal doorvoeren."
    "Je start met een inhaalslag-budget van €2.500.000. Dat klinkt veel, maar IT is peperduur."
    "Maar bezuinig je te hard? Dan betaal je later de ultieme prijs aan ransomware-groepen en de Autoriteit Persoonsgegevens."
    "Aan het einde van het kwartaal probeert een hackersgroep het bedrijf binnen te dringen. Jouw keuzes bepalen wat er dan gebeurt."

    scene bg boardroom with fade
    show sarah at left  with dissolve
    show mark  at right with dissolve
    show werknemer at center with dissolve

    s "Goedemorgen! Ik ben Sarah, uw IT-consultant voor dit kwartaal. Ik zal u door alle beveiligingsbeslissingen loodsen."
    m "Mark, CFO. Eén verzoek: houd de kosten in toom. We hebben €2,5 miljoen, maar dat moet ook nog andere gaten dichten."
    w "Lisa, ik vertegenwoordig de 800 werknemers. Wat u ook beslist – denk aan ons."

    jump deel1_identiteit

################################################################################
## 5. DEEL 1: Identiteit & Toegang
################################################################################
label deel1_identiteit:
    scene bg boardroom with dissolve
    show sarah at left
    show mark  at right

    "[[ DEEL 1 — IDENTITEIT & TOEGANG ]"
    s "We beginnen met het fundament: wie mag wat doen binnen onze systemen?"

    ## --- 5A: MFA ---
label menu_mfa:
    s "Punt één: Two-Factor Authentication (2FA/MFA). Op dit moment logt iedereen in met alleen een wachtwoord."
    m "Kost dat iets?"
    s "Een enterprise MFA-platform uitrollen voor 800 man inclusief licenties, integratie en hardware-tokens voor de magazijnmedewerkers: €120.000."

    menu:
        "Koop Enterprise MFA-platform (-€120.000)":
            if budget < 120000:
                m "Budget is ontoereikend. De bank biedt een lening van €200.000 aan (terugbetalen: €240.000)."
                menu:
                    "Accepteer lening":
                        $ aantal_leningen += 1
                        $ budget += 200000
                        $ lening += 240000
                    "Weiger lening":
                        s "Dan moeten we een andere optie kiezen voor MFA."
                        jump menu_mfa
                        
            $ budget -= 120000
            $ security_waarde += 40
            $ heeft_mfa = True
            s "Uitstekend. Elke medewerker logt nu in met wachtwoord + token. Zelfs een gelekt wachtwoord is nutteloos."
            m "Flinke uitgave, maar ik snap het."
        
        "Verplicht gratis Google Authenticator (+€0, maar reputatieverlies)":
            $ reputatie -= 10
            $ security_waarde += 20
            $ heeft_mfa = True
            s "Het werkt, maar de uitrol is een drama en 30%% van de medewerkers gaat het 'tijdelijk' overslaan omdat we het niet kunnen afdwingen."
            w "Ik vind het echt onwerkbaar zonder goede support..."
        
        "MFA overslaan, wachtwoorden zijn voldoende (+€0)":
            $ security_waarde -= 20
            s "Dat is suïcidaal. Elke phishing-aanval die een wachtwoord buitmaakt, geeft direct toegang tot het systeem."
            m "Maar het bespaart een ton. Lekker."

    ## --- 5B: Wachtwoorden ---
label menu_wachtwoorden:
    s "Punt twee: wachtwoordbeleid voor de Klantendatabase en het Admin-paneel."

    menu:
        "Koop Enterprise Password Manager licenties (-€65.000)":
            if budget < 65000:
                m "Budget is ontoereikend. De bank biedt €100.000 aan (terugbetalen: €120.000)."
                menu:
                    "Accepteer lening":
                        $ aantal_leningen += 1
                        $ budget += 100000
                        $ lening += 120000
                    "Weiger lening":
                        s "Kies dan een ander wachtwoordbeleid."
                        jump menu_wachtwoorden
                        
            $ budget -= 65000
            $ security_waarde += 35
            s "Perfect. Unieke, complexe wachtwoorden per dienst. Niemand hoeft meer iets te onthouden."
            w "Oh, dat is eigenlijk wel handig!"
        
        "Verplicht wachtwoord wijzigen elke 3 maanden (-€15.000 voor IT-support overuren)":
            $ budget -= 15000
            $ security_waarde += 5
            $ reputatie -= 15
            s "Mensen gaan 'Nexio2024!' veranderen in 'Nexio2025!'. Schijnveiligheid en de helpdesk stroomt vol."
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
                s "BEIDE wachtwoorden zijn '[ww_database]'?! Als één lek is, is ALLES lek. Een ramp in wording."
                m "Gemakkelijk te onthouden! Efficiënt!"
            elif ww_database.lower() in ["admin", "1234", "password", "nexio", "welkom", "123456"] or ww_admin.lower() in ["admin", "1234", "password", "nexio", "welkom", "123456"]:
                $ dom_wachtwoord = True
                $ security_waarde -= 40
                s "Echt?! '[ww_database]' en '[ww_admin]'? Een script raadt dit in seconden."
            else:
                $ security_waarde -= 10
                s "Ze zijn tenminste verschillend. Maar gedeelde wachtwoorden blijven extreem kwetsbaar."

    ## --- 5C: Open Google Drive ---
label menu_googledrive:
    s "Punt drie: Onze cloud-opslag. Veel klantdata staat op openbaar gedeelde links in Google Drive."

    menu:
        "Implementeer streng Cloud Security Posture Management (CSPM) (-€35.000)":
            $ budget -= 35000
            $ security_waarde += 25
            s "Slim. Geautomatiseerde controles scannen continu of we per ongeluk data openzetten naar het internet."
        
        "Laat het open, stuur een waarschuwingsmail (+€0)":
            $ open_googledrive = True
            $ security_waarde -= 15
            s "Een mailtje helpt niet. Gevoelige klantdata staat gewoon open op het internet. Google indexeert dit gewoon."
            m "Niemand weet toch hoe ze dat moeten vinden?"

    ## --- 5D: Ontslagen werknemer ---
label menu_ontslagen_werknemer:
    scene bg ceo_office with dissolve
    show ceo_c at center with dissolve
    show sarah at left

    s "Er wordt volgende week een senior ontslagen. Er bestaat geautomatiseerde Identity & Access (IAM) software die zijn toegang over de hele linie in één seconde afsluit."
    ceo_c "Kunnen we die toegang niet gewoon handmatig intrekken na het gesprek?"

    menu:
        "Koop IAM automated offboarding integratie (-€85.000)":
            if budget < 85000:
                m "Budget te laag. Lening van €100.000 nodig (terugbetalen: €120.000)."
                menu:
                    "Accepteer lening":
                        $ aantal_leningen += 1
                        $ budget += 100000
                        $ lening += 120000
                    "Weiger lening":
                        s "Dan kan je deze software niet betalen."
                        jump menu_ontslagen_werknemer
                        
            $ budget -= 85000
            $ security_waarde += 30
            $ auto_blokkering = True
            s "Duur, maar noodzakelijk. Zodra HR hem afmeldt, verliest hij letterlijk elke vorm van toegang."
        
        "Handmatig regelen via IT, duurt 48 uur (+€0)":
            $ security_waarde -= 20
            $ reputatie -= 5
            s "Een ontevreden techneut kan in 48 uur makkelijk onze hele codebase klonen of servers wissen."
            m "We hebben toch vertrouwen in onze mensen?"

    ## --- 5E: Developer admin-rechten ---
label menu_developer_admin:
    scene bg boardroom with dissolve
    show sarah at left
    show mark  at right

    s "De developers klagen. Ze willen admin-rechten op de productieomgeving. Ze weigeren steeds IT-tickets aan te maken."

    menu:
        "Geef developers volledige admin-rechten (+€0, snel)":
            $ developer_admin = True
            $ security_waarde -= 25
            $ reputatie += 5
            s "Als één dev gephisht wordt, is het hele bedrijf direct van de hacker."
        
        "Implementeer Privileged Access Management (PAM) (-€150.000)":
            if budget < 150000:
                m "Budget te laag. Lening van €200.000 (terugbetalen: €240.000) nodig."
                menu:
                    "Accepteer lening":
                        $ aantal_leningen += 1
                        $ budget += 200000
                        $ lening += 240000
                    "Weiger lening":
                        s "Je hebt hier niet genoeg budget voor."
                        jump menu_developer_admin
                        
            $ budget -= 150000
            $ security_waarde += 35
            s "Een forse investering, maar ze krijgen nu dynamisch tijdelijke admin-rechten die volledig gelogd en gefilmd worden."
        
        "Weiger, procedures blijven zoals ze zijn (+€0)":
            $ reputatie -= 10
            $ security_waarde += 10
            s "Veilig, maar de developers zijn woedend. Sommigen gaan 'creatieve' omwegen zoeken."

    jump deel2_endpoints

################################################################################
## 6. DEEL 2: Apparaten & Endpoints
################################################################################
label deel2_endpoints:
    scene bg office with fade
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[[ DEEL 2 — APPARATEN & ENDPOINTS ]"

    ## --- 6A: Updates ---
label menu_updates:
    s "Er is een kritieke update-campagne nodig voor alle 800 endpoints en 50 servers."

    menu:
        "Enterprise geautomatiseerd patchbeheer invoeren (-€75.000)":
            if budget < 75000:
                m "Budget te laag. We moeten dit overslaan."
                $ updates_genegeerd = True
                jump menu_iot
            $ budget -= 75000
            $ security_waarde += 30
            s "Alle systemen worden strak up-to-date gehouden zonder downtime."
        
        "Eenmalige handmatige update-campagne (-€15.000)":
            $ budget -= 15000
            $ security_waarde += 10
            s "Beter dan niks, maar over zes maanden staan we opnieuw achter."
        
        "Updates uitstellen tot na het kwartaal (+€0)":
            $ updates_genegeerd = True
            $ security_waarde -= 30
            s "Dit is hoe 90%% van de succesvolle hacks beginnen."
            m "Maar iedereen is productief! Geen gemopperde herstarts!"

    ## --- 6B: Onveilige IoT ---
label menu_iot:
    s "Onze 45 IP-camera's en thermostaten draaien op standaard wachtwoorden op het hoofdnetwerk."

    menu:
        "Netwerk engineering: Isoleer IoT op aparte VLANs (-€45.000)":
            if budget < 45000:
                m "Budget te laag, we slaan dit over."
                $ onveilige_iot = True
                jump menu_byod
            $ budget -= 45000
            $ security_waarde += 25
            $ onveilige_iot = False
            s "Netjes. Als een thermostaat gehackt wordt, stranden ze in dat afgesloten netwerkje."
        
        "Alleen wachtwoorden wijzigen (-€8.000)":
            $ budget -= 8000
            $ security_waarde += 10
            s "Beter, maar ze zitten nog steeds op hetzelfde netwerk als de servers. Niet ideaal."
        
        "Laat alles zoals het is (+€0)":
            $ onveilige_iot = True
            $ security_waarde -= 20
            s "Camera's zijn een favoriete voordeur voor Russische botnets."

    ## --- 6C: BYOD (eigen laptop) ---
label menu_byod:
    show werknemer at center with dissolve
    w "Mag ik tijdelijk mijn privé-laptop gebruiken? Mijn werk-laptop is stuk."

    menu:
        "Nee, bouw een pool van zakelijke leen-laptops op (-€40.000)":
            $ budget -= 40000
            $ security_waarde += 20
            w "Oh, dat is eerlijk eigenlijk."
            s "We houden schimmige privé-apparatuur mooi buiten de deur."
        
        "Ja, maar alleen via VPN en op een apart gastnetwerk (+€0)":
            $ byod_risico = False
            $ security_waarde += 5
            s "Redelijk compromis. Niet perfect, maar geïsoleerd."
        
        "Ja, gewoon op het normale netwerk (+€0)":
            $ byod_risico = True
            $ security_waarde -= 25
            s "Met één geïnfecteerde privé-laptop infecteren we straks het hele kantoor."

    ## --- 6D: CEO-laptop verloren ---
label menu_ceo_laptop:
    hide werknemer
    scene bg parking with dissolve
    show ceo_c at center with dissolve
    show sarah at left

    ceo_c "Ik heb mijn laptop met de fusie-contracten in de trein laten liggen..."

    menu:
        "We hadden Mobile Device Management & Encryptie (-€0, mits security hoog is)":
            if security_waarde >= 30:
                $ security_waarde += 10
                s "Geen paniek, schijf is versleuteld en ik wipe hem nu op afstand."
            else:
                s "Maar dat hadden we dus NIET gekocht! De data ligt op straat."
                $ reputatie -= 20
                $ security_waarde -= 20
                $ datalek = True
        
        "We hadden niets ingesteld... (reputatieschade)":
            $ reputatie -= 25
            $ security_waarde -= 25
            $ datalek = True
            s "Dit is een enorm datalek. De media gaat ons fileren en we krijgen een boete van de AP."

    jump deel3_infrastructuur

################################################################################
## 7. DEEL 3: IT-omgeving & Infrastructuur
################################################################################
label deel3_infrastructuur:
    scene bg server_room with dissolve
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[[ DEEL 3 — IT-OMGEVING & INFRASTRUCTUUR ]"

    ## --- 7A: Wifi ---
label menu_wifi:
    s "Het wifi-wachtwoord 'NeXio2019' wordt door medewerkers én gasten gebruikt op hetzelfde netwerk."

    menu:
        "802.1x implementatie & volledige netwerksegmentatie (-€60.000)":
            if budget < 60000:
                m "Geen budget."
                $ onveilige_wifi = True
                jump menu_firewall
            $ budget -= 60000
            $ security_waarde += 30
            $ onveilige_wifi = False
            s "Iedereen authenticeert nu individueel. Gasten krijgen een compleet geïsoleerde verbinding."
        
        "Alleen het wifi-wachtwoord aanpassen (+€0)":
            $ onveilige_wifi = True
            $ security_waarde -= 5
            s "Betere hygiene, maar iedereen zit nog steeds op hetzelfde netwerk."
        
        "Laat alles zoals het is (+€0)":
            $ onveilige_wifi = True
            $ security_waarde -= 25
            s "Letterlijk iedereen die op de parkeerplaats staat kan inbreken op onze servers."

    ## --- 7B: Firewall & monitoring ---
label menu_firewall:
    s "We hebben geen actieve monitoring. Als we gehackt worden, merken we het pas als alles versleuteld is."

    menu:
        "Next-Gen Firewall + 24/7 Managed SOC / SIEM (-€350.000)":
            if budget < 350000:
                m "Budget te laag. Lening van €400.000 (terugbetalen: €480.000) nodig."
                menu:
                    "Accepteer lening":
                        $ aantal_leningen += 1
                        $ budget += 400000
                        $ lening += 480000
                    "Weiger lening":
                        s "We kunnen dit niet betalen."
                        jump menu_firewall
                        
            $ budget -= 350000
            $ security_waarde += 50
            s "Een extern team monitort ons netwerk nu 24/7. De heilige graal van cybersecurity."
        
        "Alleen een nieuwe basale Firewall installeren (-€60.000)":
            $ budget -= 60000
            $ security_waarde += 20
            s "Beter, maar zonder een SOC (Security Operations Center) kijkt er niemand naar de waarschuwingen."
        
        "Niets doen (+€0)":
            $ security_waarde -= 30
            s "Gemiddeld zit een hacker 200 dagen in je netwerk voor hij toeslaat. Wij zijn letterlijk blind."

    jump deel4_applicaties

################################################################################
## 8. DEEL 4: Applicaties & Data
################################################################################
label deel4_applicaties:
    scene bg office with dissolve
    show sarah at left with dissolve
    show mark  at right with dissolve

    "[[ DEEL 4 — APPLICATIES & DATA ]"

    ## --- 8A: Sketchy software ---
label menu_sketchy_software:
    s "Finance wil software. Ze vonden een gratis 'cracked' versie of een Enterprise licentie van €45.000."
    m "Gratis is toch gratis? Het is exact dezelfde software!"

    menu:
        "Koop officiële Enterprise licentie (-€45.000)":
            $ budget -= 45000
            $ security_waarde += 15
            s "Verstandig. Geen malware, en we hebben recht op enterprise support."
        
        "Download de gratis cracked versie (+€0)":
            $ sketchy_software = True
            $ security_waarde -= 35
            s "Gefeliciteerd, we hebben zojuist vrijwillig een Russische backdoor op de finance-systemen gezet."

    ## --- 8B: Pentesting ---
label menu_pentest:
    s "We lanceren een nieuwe klantenportal. Willen we een externe partij inhuren voor een penetratietest?"

    menu:
        "Ja, huur een gerenommeerd Red Team in (-€60.000)":
            if budget < 60000:
                m "Budget te laag."
                $ pen_test_gedaan = False
                jump deel5_phishing
                
            $ budget -= 60000
            $ security_waarde += 40
            $ pen_test_gedaan = True
            s "Top. Ze hebben 2 kritieke SQL-injecties gevonden die we direct gefixt hebben."
        
        "Nee, intern team doet een snelle check (+€0)":
            $ pen_test_gedaan = False
            $ security_waarde += 5
            s "Intern team mist de hacker-mindset en tools. We gaan dingen missen."
        
        "Nee, we lanceren gewoon (+€0)":
            $ pen_test_gedaan = False
            $ security_waarde -= 20
            s "Elke scriptkiddie kan die portaal morgen overnemen."

    jump deel5_phishing

################################################################################
## 9. DEEL 5: De Phishing Mail (CEO Fraud)
################################################################################
label deel5_phishing:
    scene bg ceo_office with dissolve
    show ceo_c at center with dissolve

    "[[ DEEL 5 — MENSELIJKE FOUTEN ]"
    "Een donderdagmiddag. Je zit in je kantoor. Een mail met HOGE PRIORITEIT plopt binnen."

    mail "VAN: sarah.itconsultant.nexio@gmai1.com\nAAN: ceo@nexio-co.com\nONDERWERP: URGENT: Cloud factuur"
    mail "Beste,\n\nOnze AWS cloudservers gaan offline als de achterstallige factuur niet voor 17:00 is voldaan."
    mail "Mijn bank blokkeert overboekingen momenteel. Maak direct €185.000 over naar:\nNL99 SCAM 0123 4567 89\n\nGroet, Sarah"

    menu:
        "Maak direct €185.000 over om downtime te voorkomen (-€185.000)":
            if budget < 185000:
                "Saldo te laag. Je hebt puur geluk gehad."
            else:
                $ budget -= 185000
                $ reputatie -= 20
                $ phishing_gebeten = True
                show sarah at left with dissolve
                s "CSO? U heeft zojuist €185.000 naar een onbekende rekening in Cyprus gestuurd. Ik heb die mail nooit verstuurd."

        "Stuur naar spam en negeer (+€0)":
            $ security_waarde += 5
            show sarah at left with dissolve
            s "Goed gezien. Het adres is 'gmai1.com'. Klassieke truc."

        "Bel Sarah direct om te verifiëren (+€0, beste optie)":
            $ security_waarde += 20
            show sarah at left with dissolve
            s "Whaling-aanval (CEO Fraude)! Niet betalen. Ik blokkeer de afzender direct op de mailservers."
            
        "Betaal en stuur tegelijk een waarschuwing naar IT (+€0)":
            $ budget -= 185000
            $ reputatie -= 10
            $ phishing_gebeten = True
            $ security_waarde -= 10
            show sarah at left with dissolve
            s "U heeft al betaald... De waarschuwing is te laat. Dat geld is weg."

    jump de_aanval

################################################################################
## 10. DE HACK — De Finale
################################################################################
label de_aanval:
    scene bg server_room with pixellate
    "[[ KWARTAAL EINDIGT — DE AANVAL BEGINT ]"
    "Drie maanden later. Midden in de nacht gaat uw telefoon."

    if wachtwoorden_gelijk:
        with hpunch
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        show sarah at left
        s "CSO!! CRISIS! Een medewerker is gephisht. Omdat u voor het Admin-paneel EXACT HETZELFDE wachtwoord ('[ww_database]') had gebruikt, zijn ze overal binnen!"
        s "RANSOMWARE. Ze eisen 2 Miljoen euro in Bitcoin!"
        $ datalek = True
        $ budget -= 2000000
        $ reputatie -= 95

    elif dom_wachtwoord:
        with hpunch
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        show sarah at left
        s "Ze brute-forceden uw zwakke admin wachtwoord ('[ww_admin]') in drie seconden. Alles versleuteld!"
        $ datalek = True
        $ budget -= 1500000
        $ reputatie -= 70

    else:
        $ aanval_kracht = renpy.random.randint(30, 70)
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
            s "CSO! Ze probeerden binnen te komen, maar onze SOC en firewalls hielden ze tegen! Het netwerk is een fort!"
            if pen_test_gedaan:
                s "Ze probeerden precies die SQL-injectie die we na de pentest hebben gedicht."
            $ reputatie += 10
            if reputatie > 100:
                $ reputatie = 100
        else:
            with hpunch
            scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
            show sarah at left
            if sketchy_software:
                s "De backdoor in de cracked software gaf ze onopgemerkt toegang..."
            elif updates_genegeerd:
                s "Ze gebruikten een patch die we weigerden te installeren."
            s "De firewalls zijn doorbroken. Ze hebben de hele productiedatabase gekopieerd en versleuteld."
            $ budget -= 1200000
            $ datalek = True
            $ reputatie -= 50

    jump eindscherm

################################################################################
## 11. EINDSCHERM
################################################################################
label eindscherm:
    hide screen status_overlay
    scene bg news_flash with dissolve

    "[[ HET OORDEEL VAN DE RAAD VAN BESTUUR ]"
    ""
    "Eindbudget:    € [budget:,d]"
    if lening > 0:
        "Uitstaande schuld: € [lening:,d]"
    "Publieke reputatie: [reputatie]%%"
    "Security score: [security_waarde] punten"

    if wachtwoorden_gelijk or dom_wachtwoord:
        news "BREAKING: Megaboete Autoriteit Persoonsgegevens voor NeXio & Co wegens laks wachtwoordbeleid."
        "U bent direct ontslagen. Het incident staat in alle vakbladen als schoolvoorbeeld van wat niet moet."
    elif datalek and reputatie < 20:
        news "BREAKING: Massaal datalek bij [bedrijfsnaam]. Klanten klagen bedrijf aan. Aandelenkoers keldert 60%%."
        "U bent op staande voet ontslagen. Het herstel kost het bedrijf miljoenen."
    elif datalek:
        news "BREAKING: Ransomware-aanval kost NeXio & Co miljoenen. Klantdata gestolen."
        "U bent ontslagen wegens nalatigheid. De aanval had voorkomen kunnen worden."
    elif lening > budget:
        "U heeft de hack weerstaan, maar het bedrijf is bedolven onder leningen. De Raad is niet blij."
        "Een pyrrusoverwinning."
    elif reputatie < 40:
        "De hack is voorkomen, maar uw harde bezuinigingen en slechte communicatie hebben de reputatie vernietigd."
        "Het personeel staakt. U treedt af."
    elif reputatie < 70:
        "Een gemengd resultaat. De aanval is deels weerstaan maar er is schade. De Raad houdt u onder toezicht."
    elif security_waarde >= 150:
        "PERFECTE SCORE. U wordt door vakbladen geroemd als top CSO. Een masterclass in enterprise security."
        news "NeXio & Co weerhoudt massale cyberaanval: 'We waren klaar.'"
    else:
        "De hack is voorkomen en het bedrijf is veilig. Goed gedaan, CSO."
        "De Raad verlengt uw contract voor twee jaar."

    "[[ EINDE ]"
    return
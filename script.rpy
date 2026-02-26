################################################################################
## NEXIO & CO - Cybersecurity Game
################################################################################

################################################################################
## 1. Assets & Schalen
################################################################################
image bg office          = im.Scale("bg office.png", 1920, 1080)
image bg boardroom       = im.Scale("bg boardroom.jpg", 1920, 1080)
image bg server_room     = im.Scale("bg server_room.jpg", 1920, 1080)
image bg hack_attack     = im.Scale("bg hack_attack.jpg", 1920, 1080)
image bg news_flash      = im.Scale("bg news_flash.jpg", 1920, 1080)
image bg ceo_office      = im.Scale("bg ceo_office.jpg", 1920, 1080)

image sarah     = im.FactorScale("sarah.png", 1.8)
image mark      = im.FactorScale("mark.png", 1.8)
image ceo       = im.FactorScale("ceo.png", 1.8)
image werknemer = im.FactorScale("werknemer.png", 1.8)

################################################################################
## 2. Globale Variabelen
################################################################################
default geld            = 500000 
default reputatie       = 100
default wv_happiness    = 7
default weakness        = 0
default datalek         = False

# Deel 1 Booleans (Werknemers)
default mfa                          = False
default verschillende_wachtwoorden   = False
default phishing_awareness           = False
default updated                      = False
default admin_rechten                = True  # True is gevaarlijk
default end_of_life_systems          = True  # True is gevaarlijk
default desk_notities                = True  # True is gevaarlijk

# Deel 2 Variabelen (Infrastructuur)
default firewall         = 0
default backups          = 0
default backups_time     = 0
default eigen_laptop     = False
default security_cameras = 1

# Karakters
define s    = Character("Sarah (IT Consultant)", color="#3498db")
define m    = Character("Mark (CFO)", color="#e67e22")
define cso  = Character("Jij (CSO)", color="#9b59b6")
define ceo_c= Character("CEO", color="#f1c40f")
define w    = Character("Lisa (Werknemer)", color="#27ae60")
define w_mad= Character("Lisa (Geïrriteerd)", color="#e74c3c")
define sys  = Character("SYSTEEM", color="#ecf0f1")
define news = Character("NIEUWS", color="#e74c3c")

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
            text "--- NeXio & Co ---" size 16 bold True color "#3498db"
            hbox:
                spacing 8
                text "BUDGET:"    size 16 color "#bdc3c7"
                text "€ [geld:,d]" size 18 bold True color "#2ecc71"
            hbox:
                spacing 8
                text "REPUTATIE:" size 16 color "#bdc3c7"
                text "[reputatie]%%" size 18 bold True color "#f39c12"
            hbox:
                spacing 8
                text "WV HUMEUR:"  size 16 color "#bdc3c7"
                if wv_happiness >= 3:
                    text "[wv_happiness]/7" size 18 bold True color "#2ecc71"
                else:
                    text "[wv_happiness]/7" size 18 bold True color "#e74c3c"

################################################################################
## 4. INTRODUCTIE
################################################################################
label start:
    scene black
    show screen status_overlay

    scene bg ceo_office with fade
    show ceo_c at center with dissolve

    ceo_c "Ah, kom verder. Ga zitten. Welkom bij NeXioCo."
    ceo_c "Je weet waarom we je hebben aangenomen. Ons bedrijf is de afgelopen jaren geëxplodeerd. We hebben inmiddels 800 werknemers op de loonlijst, we draaien miljoenenomzetten, maar als ik heel eerlijk ben... onze IT-security is een gatenkaas."
    ceo_c "Daarom ben jij nu onze Chief Security Officer. Jij krijgt de leiding over ons budget en jij bepaalt vanaf vandaag welke maatregelen we wel en niet doorvoeren."
    cso "Ik ben er klaar voor. Waar beginnen we mee?"
    ceo_c "We hebben een externe IT-consultant ingehuurd. Zij heeft een lijst met mogelijke securitymaatregelen voorbereid."
    ceo_c "Het is aan jou om haar voorstellen te beoordelen. Weeg de kosten af tegen de risico's. Succes. Ze wachten op je in de vergaderzaal."

    jump deel1_werknemers

################################################################################
## 5. DEEL 1: IT Consultant & Werknemers
################################################################################
label deel1_werknemers:
    scene bg boardroom with dissolve
    show sarah at left with dissolve
    show werknemer at right with dissolve

    sys "*** DEEL 1: IDENTITEIT & TOEGANG ***"
    s "Welkom CSO. Ik ben Sarah, IT Consultant. Dit is Lisa, de Werknemersvertegenwoordiger (WV)."
    w "Hoi. Ik zeg het maar meteen: wij willen zo min mogelijk extra werk of lastige inlogprocedures."
    
    # 1. MFA
    s "Laten we beginnen met Multi-Factor Authenticatie (MFA)."
    menu:
        "Wil je Multifactorauthenticatie aanleggen voor alle medewerkers?"
        
        "Geen MFA (Niets)":
            $ mfa = False
            s "Risicovol, maar we doen niets."
            
        "Optionele MFA (50%% kans dat ze het gebruiken)":
            $ kans = renpy.random.randint(1, 100)
            if kans <= 50:
                $ mfa = True
            else:
                $ mfa = False
            s "We hebben het aangeraden. Ongeveer de helft heeft het ingesteld."
            
        "Verplichte MFA (WV -1)":
            $ mfa = True
            $ wv_happiness -= 1
            $ reputatie -= 5
            s "Iedereen is nu verplicht MFA te gebruiken."
            w "Dit kost ons elke ochtend zoveel extra tijd..."

    # 2. Wachtwoorden
    s "Punt 2: Wachtwoorden. Iedereen gebruikt nu overal hetzelfde wachtwoord."
    menu:
        "Hoe pakken we de wachtwoorden aan?"
        
        "Dezelfde wachtwoorden zijn toegestaan (Niets)":
            $ verschillende_wachtwoorden = False
            s "Makkelijk voor de werknemers, een droom voor hackers."
            
        "Gelijkaardige wachtwoorden toegestaan (Niets)":
            $ verschillende_wachtwoorden = False
            s "Nexio1 en Nexio2... het is iets beter, maar niet veel."
            
        "Verschillende en complexe wachtwoorden VERPLICHT (WV -1)":
            $ verschillende_wachtwoorden = True
            $ wv_happiness -= 1
            $ reputatie -= 5
            s "Veiliger, maar dit gaan ze niet onthouden."
            
            # 2.1 Password Manager (Sub-menu)
            menu:
                "Bieden we een Password Manager aan?"
                
                "Niet toegestaan (WV -1)":
                    $ wv_happiness -= 1
                    $ reputatie -= 5
                    w "Dus we moeten 20 moeilijke wachtwoorden onthouden zonder hulpmiddel?! Schandalig!"
                "Gratis variant gebruiken (+€0)":
                    s "Beter dan niks, maar beperkte controle voor IT."
                "Betaalde Enterprise variant (-€15.000)":
                    $ geld -= 15000
                    s "Top, dit maakt het veilig én makkelijk."

    # 3. Phishing Awareness
    s "Punt 3: Phishing Awareness Training."
    menu:
        "Laat de werknemers geen training doen (25%% kans op awareness)":
            if renpy.random.randint(1, 100) <= 25:
                $ phishing_awareness = True
            else:
                $ phishing_awareness = False
            s "We hopen dat ze zelf slim genoeg zijn."
            
        "Verplicht de training (-€5.000, 75%% kans op awareness, WV -1)":
            $ geld -= 5000
            $ wv_happiness -= 1
            $ reputatie -= 5
            if renpy.random.randint(1, 100) <= 75:
                $ phishing_awareness = True
            else:
                $ phishing_awareness = False
            s "Training is ingepland."

    # 4. Updates
    s "Punt 4: Software updates."
    menu:
        "Laat ze niets doen":
            $ updated = False
            
        "Forceer Auto-Update op de achtergrond":
            $ updated = True
            s "Updates draaien nu stil op de achtergrond."
            
        "Forceer werknemers om updates altijd EERST te doen (WV -1)":
            $ updated = True
            $ wv_happiness -= 1
            $ reputatie -= 5
            w "Midden in een meeting opnieuw opstarten? Belachelijk!"

    # 5. Fingerprint
    s "Punt 5: Vingerafdrukscanners op de laptops."
    menu:
        "Niet invoeren":
            pass
        "Wel invoeren (-€20.000, MFA=True, WV -1)":
            $ geld -= 20000
            $ mfa = True
            $ wv_happiness -= 1
            $ reputatie -= 5
            s "Biometrische beveiliging is actief."

    # 6. Admin Rechten
    s "Punt 6: Developers klagen dat ze geen admin-rechten hebben."
    menu:
        "Geef niemand rechten (WV -1)":
            $ admin_rechten = False
            $ wv_happiness -= 1
            $ reputatie -= 5
            w "De devs kunnen zo hun werk niet doen!"
            
        "Alleen de teamleaders (50%% kans op admin rechten)":
            if renpy.random.randint(1, 100) <= 50:
                $ admin_rechten = True
            else:
                $ admin_rechten = False
                
        "Geef iedereen admin-rechten":
            $ admin_rechten = True
            s "Erg gevaarlijk, maar ze zijn blij."

    # 7. End-of-life systems
    s "Punt 7: We gebruiken nog verouderde 'End-of-Life' systemen."
    menu:
        "Niet aanpassen (Niets)":
            $ end_of_life_systems = True
            
        "Wel aanpassen (-€30.000, WV -1)":
            $ geld -= 30000
            $ end_of_life_systems = False
            $ wv_happiness -= 1
            $ reputatie -= 5
            w "Moeten we alweer nieuwe software leren?!"

    # 8. Screen lock
    s "Punt 8: Automatische schermvergrendeling als iemand wegloopt."
    menu:
        "Niet instellen":
            pass
        "Na 10 minuten (WV -1)":
            $ wv_happiness -= 1
            $ reputatie -= 5
        "Na 30 seconden (WV -1)":
            $ wv_happiness -= 1
            $ reputatie -= 5
            s "Veilig, maar ze moeten wel heel vaak inloggen."

    # 9. Clean Desk
    s "Punt 9: Clean Desk Policy."
    menu:
        "Alle notities zijn toegestaan":
            $ desk_notities = True
        "Geen wachtwoorden, wel andere notities":
            $ desk_notities = False
        "Helemaal GEEN notities op het bureau (WV -1)":
            $ desk_notities = False
            $ wv_happiness -= 1
            $ reputatie -= 5

    # CHECK WV HAPPINESS (De rebellie!)
    if wv_happiness <= 0:
        sys "!!! WAARSCHUWING !!!"
        sys "De werknemers zijn woedend over alle strenge regels (Humeur <= 0). Ze beginnen massaal beleid te negeren en systemen te omzeilen!"
        
        # 50% chance to turn each True security measure to False
        if mfa and renpy.random.randint(1, 100) <= 50:
            $ mfa = False
            sys "MFA wordt massaal omzeild."
        if verschillende_wachtwoorden and renpy.random.randint(1, 100) <= 50:
            $ verschillende_wachtwoorden = False
            sys "Wachtwoorden worden stiekem weer gedeeld."
        if phishing_awareness and renpy.random.randint(1, 100) <= 50:
            $ phishing_awareness = False
            sys "Niemand let meer op tijdens de verplichte trainingen."
        if updated and renpy.random.randint(1, 100) <= 50:
            $ updated = False
            sys "Updates worden geblokkeerd door werknemers."

    jump deel2_infrastructuur


################################################################################
## 6. DEEL 2: IT Consultant & CFO (Infrastructuur)
################################################################################
label deel2_infrastructuur:
    scene bg boardroom with dissolve
    hide werknemer
    show mark at right with dissolve

    sys "*** DEEL 2: INFRASTRUCTUUR & KOSTEN ***"
    m "Ik ben Mark, CFO. Reputatie is leuk, maar geld is beter. Elke grote uitgave schaadt onze aandeelhouderswaarde (-10 reputatie)."
    
    # 1. Firewall
    s "We moeten beslissen over de Firewall."
    menu:
        "Geen firewall (€0)":
            $ firewall = 0
        "Goedkope firewall (-€10.000)":
            $ firewall = 1
            $ geld -= 10000
        "Duurdere maar goede firewall (-€50.000, Reputatie -5)":
            $ firewall = 2
            $ geld -= 50000
            $ reputatie -= 5
        "Hele dure Enterprise firewall (-€150.000, Reputatie -10)":
            $ firewall = 3
            $ geld -= 150000
            $ reputatie -= 10
            m "Absurd duur!"

    # 2. Backups
    s "Hoe regelen we de Backups?"
    menu:
        "Geen backups (€0)":
            $ backups = 0
            
        "Alleen belangrijke files (-€10.000)":
            $ backups = 1
            $ geld -= 10000
            
        "Alle files backuppen (-€150.000, Reputatie -10)":
            $ backups = 2
            $ geld -= 150000
            $ reputatie -= 10

    if backups > 0:
        menu:
            "Hoe vaak maken we deze backup?"
            "Elk jaar (-€2.000)":
                $ backups_time = 1
                $ geld -= 2000
            "Elke maand (-€8.000)":
                $ backups_time = 2
                $ geld -= 8000
            "Elke week (-€10.000)":
                $ backups_time = 3
                $ geld -= 10000
            "Elke dag (-€50.000, Reputatie -5)":
                $ backups_time = 4
                $ geld -= 50000
                $ reputatie -= 5
                
        menu:
            "Waar slaan we dit op?"
            "Externe servers (-€10.000)":
                $ geld -= 10000
            "Interne eigen servers (-€50.000, Reputatie -5)":
                $ geld -= 50000
                $ reputatie -= 5

    # 3. Eigen laptops (BYOD)
    s "Staan we toe dat werknemers eigen laptops gebruiken?"
    menu:
        "Nee (Geen kosten)":
            $ eigen_laptop = False
        "Ja, regel de infrastructuur hiervoor (-€150.000, Reputatie -10)":
            $ eigen_laptop = True
            $ geld -= 150000
            $ reputatie -= 10

    # 4. Security Cameras
    s "Wat doen we met de verouderde security camera's?"
    menu:
        "Huidige laten hangen (€0)":
            $ security_cameras = 1
        "Verwijderen en niet vervangen (€0)":
            $ security_cameras = 0
        "Verwijderen en vervangen door nieuwe (-€50.000, Reputatie -5)":
            $ security_cameras = 2
            $ geld -= 50000
            $ reputatie -= 5

    if security_cameras > 0:
        menu:
            "Huren we een security team in om de camera's te bekijken?"
            "Nee (€0)":
                pass
            "Nee, alleen slimme sensoren (-€5.000)":
                $ geld -= 5000
            "Alleen overdag (-€10.000)":
                $ geld -= 10000
            "Overdag en 's nachts (-€50.000, Reputatie -5)":
                $ geld -= 50000
                $ reputatie -= 5
            "24/7 bewakingsteam (-€150.000, Reputatie -10)":
                $ geld -= 150000
                $ reputatie -= 10

    jump deel3_hack

################################################################################
## 7. DEEL 3: DE HACK (De Gevolgen)
################################################################################
label deel3_hack:
    scene bg office with fade
    hide mark
    show werknemer at right with dissolve

    sys "*** DEEL 3: DE AANVAL ***"
    
    # 3.0 IoT Printer Scenario
    sys "[ IoT PRINTER AANVAL DETECTIE ]"
    s "CSO! Een netwerkprinter is zojuist uitgevallen en IT merkt verdachte activiteit. De printer is gecompromitteerd en dient nú als toegangspunt voor een cyberaanval!"
    menu:
        "Probleem negeren en andere printers gebruiken":
            $ reputatie -= 20
            $ geld -= 45000
            $ weakness += 2
            s "De aanval verspreidt zich verder over het netwerk..."
            
        "Een goedkope printer aankopen (-€70k, Reputatie -25%)":
            $ reputatie -= 25
            $ geld -= 70000
            $ weakness += 2
            s "Dit nieuwe, goedkope toestel vormt direct een extra risico!"
            
        "Een betrouwbare bedrijfsprinter aankopen (-€20k, Reputatie -10%)":
            $ reputatie -= 10
            $ geld -= 20000
            $ weakness += 1
            s "De aanval loopt nog even, maar de impact is beperkt."
            
        "Toestel isoleren en IT onderzoek laten uitvoeren (-€12k, Reputatie -5%)":
            $ reputatie -= 5
            $ geld -= 12000
            s "Perfect. De aanval is gestopt voordat er data verloren ging."

    # 3.1 Phishing Mail
    if phishing_awareness:
        w "Hé, ik kreeg net een hele rare mail over een openstaande factuur. Ik heb hem direct gerapporteerd bij IT!"
        $ reputatie += 10
        s "Geweldig, de Phishing Awareness training werpt zijn vruchten af."
    else:
        w "Oeps... ik heb net op een link geklikt in een mailtje en per ongeluk mijn wachtwoord ingevuld..."
        menu:
            "Doe niets":
                $ weakness += 1
                if not verschillende_wachtwoorden:
                    $ weakness += 2
            "Forceer de werknemer om DIT wachtwoord aan te passen (Reputatie -5)":
                $ reputatie -= 5
                if not verschillende_wachtwoorden:
                    $ weakness += 2
            "Forceer de werknemer om AL zijn wachtwoorden aan te passen (Reputatie -15)":
                $ reputatie -= 15
                s "Gedaan. We hebben het risico geminimaliseerd."

    # 3.2 Updates & Weakness
    hide werknemer
    scene bg ceo_office with dissolve
    show ceo_c at right with dissolve

    if updated:
        s "Goed nieuws: Omdat we onze systemen hebben geüpdatet, ketsen veel geautomatiseerde aanvallen nu af."
        $ reputatie += 5
    else:
        s "CSO, we missen kritieke beveiligingspatches. Er wordt actief naar onze systemen gescand."
        $ weakness += 1
        $ reputatie -= 5
        menu:
            "Doe niets (Weakness +1, Reputatie -5)":
                $ weakness += 1
                $ reputatie -= 5
            "Forceer iedereen NU te updaten (Reputatie -10)":
                $ reputatie -= 10
                s "Dit veroorzaakt veel downtime, maar het dicht de gaten."

    # 3.3 De Grote Aanval
    scene bg server_room with hpunch
    if not mfa:
        $ weakness += 1
        
    sys "!!! CYBER AANVAL GEDETECTEERD !!!"

    # Scenario 1: Ransomware Domino (Worst Case)
    if not phishing_awareness and not updated and backups == 0 and firewall == 0:
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        s "GAME OVER! Een werknemer klikte op een link, we hadden geen firewall om het te blokkeren, en geen updates."
        s "Ransomware heeft ALLES versleuteld. Omdat we geen back-ups hebben, is het bedrijf failliet."
        $ geld -= 1000000
        $ reputatie -= 80
        jump eindscherm

    # Scenario 2: Oude Dataleak (Credential Stuffing)
    elif not verschillende_wachtwoorden and not mfa:
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        s "DATABREACH! Hackers vonden oude wachtwoorden online. Omdat we dezelfde wachtwoorden toestaan en geen MFA hebben, wandelden ze zo naar binnen!"
        $ geld -= 300000
        $ reputatie -= 50
        jump eindscherm

    # Scenario 4: De Stille Indringer (Worm)
    elif firewall == 0 and not updated:
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        s "WORM VIRUS! Omdat de firewall uit staat en de servers on-gepatcht zijn, is een geautomatiseerd virus binnengekomen. Alles ligt plat."
        $ geld -= 250000
        $ reputatie -= 40
        jump eindscherm

    # Scenario 3: Gered door de bel (MFA redt de dag)
    elif not phishing_awareness and mfa:
        s "Een werknemer vulde zijn wachtwoord in op een nepsite... Maar de aanval faalt! De hackers hadden de 2FA code op de telefoon niet."
        sys "Waarschuwing: Iemand probeerde in te loggen met jouw wachtwoord. Verander dit direct!"
        $ reputatie += 15
        jump eindscherm

    # Scenario 5: Gered door de Back-up
    elif weakness >= 3 and backups > 0:
        scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
        s "De systemen zijn geraakt door ransomware... we liggen plat!"
        s "Wacht! Gelukkig hebben we back-ups ingesteld. IT zet de boel terug. We verliezen wat tijd, maar de data is veilig en we betalen de hackers geen cent."
        $ geld -= 50000
        $ reputatie -= 10
        jump eindscherm

    # Standaard evaluatie op basis van Weakness
    else:
        if weakness >= 4:
            scene bg hack_attack with Fade(0.1, 0.0, 0.5, color="#ff0000")
            s "Ze zijn binnen! Onze verdediging was te zwak."
            $ geld -= 200000
            $ reputatie -= 40
        else:
            s "We werden aangevallen, maar onze security lagen hielden stand!"
            $ reputatie += 20

    jump eindscherm

################################################################################
## 8. EINDSCHERM
################################################################################
label eindscherm:
    hide screen status_overlay
    scene bg news_flash with dissolve

    sys "*** EINDE VAN HET KWARTAAL ***"
    
    if reputatie > 100:
        $ reputatie = 100
        
    "Eindbudget:    € [geld:,d]"
    "Publieke reputatie: [reputatie]%%"

    if geld < 0:
        news "NeXio & Co zwaar in de schulden door ongecontroleerde IT-uitgaven of gigantische ransomware betalingen."
    elif reputatie < 30:
        news "Werknemers en klanten verliezen al het vertrouwen in NeXio & Co na wanbeleid van kersverse CSO."
    elif reputatie >= 80 and geld > 100000:
        news "NeXio & Co prijst uitstekend security beleid. CSO ontvangt vette bonus!"
    else:
        news "NeXio & Co overleeft roerig kwartaal. Beveiliging is adequaat maar er is ruimte voor verbetering."

    "Bedankt voor het spelen!"
    return
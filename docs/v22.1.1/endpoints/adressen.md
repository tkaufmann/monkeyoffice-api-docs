## Adressen

[]{#adressen_Datenstrukturen .anchor}

### Datenstrukturen von Adressen

[]{#Parameter_KontaktRolle .anchor}

::: jsonproto
[KontaktRolle]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| { [\"KontaktRolle\"]{.jsonkey tag="KontaktRolle"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------------------------ |
|                                                                         |   Aufzählung, Integer                 19=[Briefe]{tag="Briefe"}\                                         |
|                                                                         |                                       1=[Verkauf(allgemein)]{tag="Verkauf(allgemein)"}\                  |
|                                                                         |                                       4=[Angebote]{tag="Angebote"}\                                      |
|                                                                         |                                       5=[Auftragsbestätigungen]{tag="Auftragsbestätigungen"}\            |
|                                                                         |                                       6=[Lieferscheine]{tag="Lieferscheine"}\                            |
|                                                                         |                                       10=[Verkaufsrechnungen]{tag="Verkaufsrechnungen"}\                 |
|                                                                         |                                       9=[Abschlagsrechnungen]{tag="Abschlagsrechnungen"}\                |
|                                                                         |                                       7=[Korrekturrechnungen]{tag="Korrekturrechnungen"}\                |
|                                                                         |                                       8=[Proformarechnungen]{tag="Proformarechnungen"}\                  |
|                                                                         |                                       11=[Storno Verkaufsrechnungen]{tag="Storno Verkaufsrechnungen"}\   |
|                                                                         |                                       2=[Einkauf(allgemein)]{tag="Einkauf(allgemein)"}\                  |
|                                                                         |                                       12=[Bestellanfragen]{tag="Bestellanfragen"}\                       |
|                                                                         |                                       13=[Bestellungen]{tag="Bestellungen"}\                             |
|                                                                         |                                       14=[Wareneingänge]{tag="Wareneingänge"}\                           |
|                                                                         |                                       15=[Lieferantengutschriften]{tag="Lieferantengutschriften"}\       |
|                                                                         |                                       16=[Rücksendungen]{tag="Rücksendungen"}\                           |
|                                                                         |                                       17=[Eingangsrechnungen]{tag="Eingangsrechnungen"}\                 |
|                                                                         |                                       18=[Storno Eingangsrechnungen]{tag="Storno Eingangsrechnungen"}\   |
|                                                                         |                                       3=[Mahnungen]{tag="Mahnungen"}                                     |
|                                                                         |                                                                                                          |
|                                                                         |   ----------------------------------- ------------------------------------------------------------------ |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KontaktRolleItem .anchor}

::: jsonproto
[KontaktRolleItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
|   ------------------------------------------------------ ---------    |
|     [\"KontaktRolle\"]{.jsonkey}: [ \... ]{.jsonvalue}   integer      |
|   ------------------------------------------------------ ---------    |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseStatus .anchor}

::: jsonproto
[AdresseStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| { [\"AdresseStatus\"]{.jsonkey tag="AdresseStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------------------------------------------ |
|                                                                           |   Aufzählung, Integer                 -2=[ohne Status]{tag="ohne Status"}\                                                 |
|                                                                           |                                       0=[Ist kein Kunde bzw. Lieferant]{tag="Ist kein Kunde bzw. Lieferant"}\              |
|                                                                           |                                       -1=[Ist Kunde bzw. Lieferant]{tag="Ist Kunde bzw. Lieferant"}\                       |
|                                                                           |                                       1=[Ist aktiver Kunde bzw. Lieferant]{tag="Ist aktiver Kunde bzw. Lieferant"}\        |
|                                                                           |                                       2=[Ist inaktiver Kunde bzw. Lieferant]{tag="Ist inaktiver Kunde bzw. Lieferant"}\    |
|                                                                           |                                       3=[Ist gesperrter Kunde bzw. Lieferant]{tag="Ist gesperrter Kunde bzw. Lieferant"}   |
|                                                                           |                                                                                                                            |
|                                                                           |   ----------------------------------- ------------------------------------------------------------------------------------ |
+---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AdressePreisAngabe .anchor}

::: jsonproto
[AdressePreisAngabe]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"AdressePreisAngabe\"]{.jsonkey tag="AdressePreisAngabe"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                     |   Aufzählung, Integer                 0=[Standard]{tag="Standard"}\       |
|                                                                                     |                                       1=[Netto]{tag="Netto"}\             |
|                                                                                     |                                       2=[Brutto]{tag="Brutto"}            |
|                                                                                     |                                                                           |
|                                                                                     |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseItem .anchor}

::: jsonproto
[AdresseItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                  |
|                                                                                                                                                                                    |
|   -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string, readonly                                                                                |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string, readonly                                                                                |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"AdressNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"Kategorie\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, eine oder mehrere Kategorien, kommagtrennt                                              |
|     [\"KundenStatus\"]{.jsonkey}: [\...]{.jsonvalue},                              [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}                                      |
|     [\"LieferantenStatus\"]{.jsonkey}: [\...]{.jsonvalue},                         [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}                                      |
|     [\"RA_Firma1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, RA = Rechnunganschrift                                                                  |
|     [\"RA_Firma2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"RA_Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"RA_Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"RA_Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"RA_Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"RA_Plz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                          |
|     [\"RA_Ort\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                          |
|     [\"RA_Geschlecht\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string, w\|m                                                                                    |
|     [\"RA_Strasse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"RA_StrasseNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"RA_Land\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                          |
|     [\"RA_LandISO\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"RA_PostfachPlz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                                          |
|     [\"RA_PostfachNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                                                          |
|     [\"RA_PfVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"RA_Telefon1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"RA_Telefon2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"RA_Telefon3\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"RA_Telefax\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"RA_Email\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"RA_Internet\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"LA_Firma1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, LA = Lieferanschrift                                                                    |
|     [\"LA_Firma2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"LA_LaVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"LA_Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"LA_Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"LA_Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"LA_Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"LA_Strasse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"LA_StrasseNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"LA_Plz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                          |
|     [\"LA_Ort\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                          |
|     [\"LA_Land\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                          |
|     [\"LA_PostfachPlz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                                          |
|     [\"LA_PostfachNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                                                          |
|     [\"LA_PfVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"LA_Telefon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"LA_Telefax\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"LA_Email\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"LA_Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"KF_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                integer, KF = Kunde Faktura                                                                     |
|     [\"KF_Sammelkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"KF_Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                          |
|     [\"KF_Ertragkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                         |
|     [\"KF_Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"KF_FinanzKonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                         |
|     [\"KF_Preisangabe\"]{.jsonkey}: [\...]{.jsonvalue},                            [AdressePreisAngabe](#Parameter_AdressePreisAngabe){.navlinkcomment}                            |
|     [\"KF_KoSt1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"KF_KoSt2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"KF_ExterneNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"KF_Lieferstopp\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"KF_Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"KF_PreislisteID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                                          |
|     [\"KF_Bankdaten\"]{.jsonkey}: [ { \"BankdatenItem\": {\...} } ]{.jsonvalue},   [BankdatenItem](#Parameter_BankdatenItem){.navlinkcomment}                                      |
|     [\"LF_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                integer, LF = Lieferant Faktura                                                                 |
|     [\"LF_Sammelkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"LF_Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                          |
|     [\"LF_Aufwandkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                         integer                                                                                         |
|     [\"LF_Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"LF_FinanzKonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                         |
|     [\"LF_Preisangabe\"]{.jsonkey}: [\...]{.jsonvalue},                            [AdressePreisAngabe](#Parameter_AdressePreisAngabe){.navlinkcomment}                            |
|     [\"LF_KoSt1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"LF_KoSt2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                          |
|     [\"LF_ExterneNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"LF_Bestellstopp\"]{.jsonkey}: [ \... ]{.jsonvalue},                         boolean (true\|false)                                                                           |
|     [\"LF_Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                          |
|     [\"LF_Bankdaten\"]{.jsonkey}: [ { \"BankdatenItem\": {\...} } ]{.jsonvalue},   [BankdatenItem](#Parameter_BankdatenItem){.navlinkcomment}                                      |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                            [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}                                        |
|     [\"UStID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                               string                                                                                          |
|     [\"Belegsprache\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                          |
|     [\"Briefanrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                          |
|     [\"Briefgruss\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                          |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                          |
|     [\"Mail_Preferred\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                           |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                    Array vom Typ string, readonly                                                                  |
|     [\"Belegausgabe\"]{.jsonkey}: [ \... ]{.jsonvalue},                            [BelegAusgabe](#Parameter_BelegAusgabe){.navlinkcomment}, readonly, neu ab Version 22.0         |
|     [\"ERechnungProfil\"]{.jsonkey}: [ \... ]{.jsonvalue},                         [ERechnungProfil](#Parameter_ERechnungProfil){.navlinkcomment}, readonly, neu ab Version 22.0   |
|     [\"LeitwegID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}                            string, readonly, neu ab Version 22.1                                                           |
|   -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                    |
| }                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseAddItem .anchor}

::: jsonproto
[AdresseAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                           |
|                                                                                                                                                                                             |
|   -------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"AdressNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"Kategorie\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, eine oder mehrere Kategorien, kommagtrennt                                                       |
|     [\"KundenStatus\"]{.jsonkey}: [\...]{.jsonvalue},                              [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}                                               |
|     [\"LieferantenStatus\"]{.jsonkey}: [\...]{.jsonvalue},                         [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}                                               |
|     [\"RA_Firma1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, RA = Rechnunganschrift                                                                           |
|     [\"RA_Firma2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"RA_Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"RA_Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"RA_Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"RA_Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"RA_Plz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                                   |
|     [\"RA_Ort\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                                   |
|     [\"RA_Geschlecht\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string, w\|m                                                                                             |
|     [\"RA_Strasse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"RA_StrasseNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"RA_Land\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                                   |
|     [\"RA_LandISO\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"RA_PostfachPlz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                                                   |
|     [\"RA_PostfachNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                                                                   |
|     [\"RA_PfVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"RA_Telefon1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"RA_Telefon2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"RA_Telefon3\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"RA_Telefax\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"RA_Email\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"RA_Internet\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"LA_Firma1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, LA = Lieferanschrift                                                                             |
|     [\"LA_Firma2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"LA_LaVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"LA_Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"LA_Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"LA_Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"LA_Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"LA_Strasse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"LA_StrasseNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"LA_Plz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                                   |
|     [\"LA_Ort\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                              string                                                                                                   |
|     [\"LA_Land\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                                   |
|     [\"LA_PostfachPlz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                                                   |
|     [\"LA_PostfachNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                                                                   |
|     [\"LA_PfVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"LA_Telefon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"LA_Telefax\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"LA_Email\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"LA_Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"KF_Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, KF = Kunde Faktura                                                                               |
|     [\"KF_Preisangabe\"]{.jsonkey}: [\...]{.jsonvalue},                            [AdressePreisAngabe](#Parameter_AdressePreisAngabe){.navlinkcomment}                                     |
|     [\"KF_ExterneNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"KF_Lieferstopp\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"KF_Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"KF_KoSt1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"KF_KoSt2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"KF_PreislisteID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                                                   |
|     [\"KF_Ertragkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                                  |
|     [\"KF_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                integer                                                                                                  |
|     [\"KF_Sammelkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"KF_Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"KF_FinanzKonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                                  |
|     [\"KF_Bankdaten\"]{.jsonkey}: [ { \"BankdatenItem\": {\...} } ]{.jsonvalue},   [BankdatenItem](#Parameter_BankdatenItem){.navlinkcomment}, beim Setzen findet keine Validierung statt   |
|     [\"LF_Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, LF = Lieferant Faktura                                                                           |
|     [\"LF_Preisangabe\"]{.jsonkey}: [\...]{.jsonvalue},                            [AdressePreisAngabe](#Parameter_AdressePreisAngabe){.navlinkcomment}                                     |
|     [\"LF_ExterneNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"LF_Bestellstopp\"]{.jsonkey}: [ \... ]{.jsonvalue},                         boolean (true\|false)                                                                                    |
|     [\"LF_Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                                                                   |
|     [\"LF_KoSt1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"LF_KoSt2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                            string                                                                                                   |
|     [\"LF_Aufwandkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                         integer                                                                                                  |
|     [\"LF_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                integer                                                                                                  |
|     [\"LF_Sammelkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"LF_Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"LF_FinanzKonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                                                                  |
|     [\"LF_Bankdaten\"]{.jsonkey}: [ { \"BankdatenItem\": {\...} } ]{.jsonvalue},   [BankdatenItem](#Parameter_BankdatenItem){.navlinkcomment}, beim Setzen findet keine Validierung statt   |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                            [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}                                                 |
|     [\"UStID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                               string                                                                                                   |
|     [\"Belegsprache\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                                                   |
|     [\"Briefanrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                                                   |
|     [\"Briefgruss\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                                                   |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                             string                                                                                                   |
|     [\"Mail_Preferred\"]{.jsonkey}: [ \... ]{.jsonvalue},                          boolean (true\|false)                                                                                    |
|     [\"Belegausgabe\"]{.jsonkey}: [ \... ]{.jsonvalue},                            [BelegAusgabe](#Parameter_BelegAusgabe){.navlinkcomment}, neu ab Version 22.0                            |
|     [\"ERechnungProfil\"]{.jsonkey}: [ \... ]{.jsonvalue},                         [ERechnungProfil](#Parameter_ERechnungProfil){.navlinkcomment}, neu ab Version 22.0                      |
|     [\"LeitwegID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}                            string, neu ab Version 22.1                                                                              |
|   -------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                             |
| }                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseListItem .anchor}

::: jsonproto
[AdresseListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                         |
|                                                                                                                           |
|   ---------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                       |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                       |
|     [\"AdressNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                       |
|     [\"Kategorie\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                       |
|     [\"KundenStatus\"]{.jsonkey}: [\...]{.jsonvalue},        [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}   |
|     [\"LieferantenStatus\"]{.jsonkey}: [\...]{.jsonvalue},   [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}   |
|     [\"RA_Firma1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, RA = Rechnunganschrift                               |
|     [\"RA_Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                       |
|     [\"RA_Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"RA_Plz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                       |
|     [\"RA_Ort\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                       |
|     [\"RA_Strasse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                       |
|     [\"RA_StrasseNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string                                                       |
|   ---------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                           |
| }                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseKategorieItem .anchor}

::: jsonproto
[AdresseKategorieItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
|   -------------------------------------------------- --------         |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string           |
|   -------------------------------------------------- --------         |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+
:::

\
[]{#Parameter_AdresseFilter .anchor}

::: jsonproto
[AdresseFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                              |
|                                                                                                                                |
|   --------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                       |
|     [\"AdresseKategorie\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"LieferantenStatus\"]{.jsonkey}: [\...]{.jsonvalue},        [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}   |
|     [\"KundenStatus\"]{.jsonkey}: [\...]{.jsonvalue}              [AdresseStatus](#Parameter_AdresseStatus){.navlinkcomment}   |
|   --------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                                |
| }                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AnsprechpartnerListItem .anchor}

::: jsonproto
[AnsprechpartnerListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------+
| {                                                                            |
|                                                                              |
|   ----------------------------------------------------------------- -------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string   |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string   |
|     [\"Abteilung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string   |
|     [\"Position\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string   |
|     [\"Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string   |
|     [\"Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string   |
|     [\"EmailFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string   |
|     [\"EmailPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string   |
|     [\"TelefonFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string   |
|     [\"TelefonMobil\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string   |
|     [\"TelefonPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}         string   |
|   ----------------------------------------------------------------- -------- |
|                                                                              |
| }                                                                            |
+------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AnsprechpartnerAddItem .anchor}

::: jsonproto
[AnsprechpartnerAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                  |
|                                                                                                                                                                                    |
|   ----------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                           |
|     [\"Abteilung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                          string                                                                           |
|     [\"Position\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                           string                                                                           |
|     [\"Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                            string                                                                           |
|     [\"Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                           string                                                                           |
|     [\"EmailFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                           |
|     [\"EmailPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                        string                                                                           |
|     [\"TelefonFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string                                                                           |
|     [\"TelefonMobil\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string                                                                           |
|     [\"TelefonPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                      string                                                                           |
|     [\"Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                             string                                                                           |
|     [\"Geschlecht\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                           |
|     [\"Geburtsdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       date (yyyy-mm-dd)                                                                |
|     [\"Briefanrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                        string                                                                           |
|     [\"Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                             string                                                                           |
|     [\"Bemerkung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                          string                                                                           |
|     [\"KontaktRollenList\"]{.jsonkey}: [ { \"KontaktRolleItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KontaktRolleItem](#Parameter_KontaktRolleItem){.navlinkcomment}   |
|   ----------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                                                    |
| }                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AnsprechpartnerItem .anchor}

::: jsonproto
[AnsprechpartnerItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                  |
|                                                                                                                                                                                    |
|   ----------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string, readonly                                                                 |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                 string, readonly                                                                 |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string, readonly                                                                 |
|     [\"Abteilung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                          string                                                                           |
|     [\"Position\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                           string                                                                           |
|     [\"Vorname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                            string                                                                           |
|     [\"Nachname\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                           string                                                                           |
|     [\"EmailFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                           |
|     [\"EmailPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                        string                                                                           |
|     [\"TelefonFirma\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string                                                                           |
|     [\"TelefonMobil\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string                                                                           |
|     [\"TelefonPrivat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                      string                                                                           |
|     [\"Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                             string                                                                           |
|     [\"Geschlecht\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                           |
|     [\"Geburtsdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       date (yyyy-mm-dd)                                                                |
|     [\"Briefanrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                        string                                                                           |
|     [\"Zusatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                             string                                                                           |
|     [\"Bemerkung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                          string                                                                           |
|     [\"KontaktRollenList\"]{.jsonkey}: [ { \"KontaktRolleItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KontaktRolleItem](#Parameter_KontaktRolleItem){.navlinkcomment}   |
|   ----------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                                                    |
| }                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BankdatenItem .anchor}

::: jsonproto
[BankdatenItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
|   ----------------------------------------------------- --------      |
|     [\"IBAN\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string        |
|     [\"BIC\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string        |
|     [\"Bank\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string        |
|     [\"Inhaber\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string        |
|   ----------------------------------------------------- --------      |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatArt .anchor}

::: jsonproto
[SepaMandatArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| { [\"SepaMandatArt\"]{.jsonkey tag="SepaMandatArt"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------ |
|                                                                           |   Aufzählung, Integer                 1=[Basislastschrift]{tag="Basislastschrift"}\    |
|                                                                           |                                       2=[Firmenlastschrift]{tag="Firmenlastschrift"}   |
|                                                                           |                                                                                        |
|                                                                           |   ----------------------------------- ------------------------------------------------ |
+---------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatTyp .anchor}

::: jsonproto
[SepaMandatTyp]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+------------------------------------------------------------------------------+
| { [\"SepaMandatTyp\"]{.jsonkey tag="SepaMandatTyp"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------- |
|                                                                           |   Aufzählung, Integer                 1=[Einmalig]{tag="Einmalig"}\          |
|                                                                           |                                       2=[Wiederholung]{tag="Wiederholung"}   |
|                                                                           |                                                                              |
|                                                                           |   ----------------------------------- -------------------------------------- |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatStatus .anchor}

::: jsonproto
[SepaMandatStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"SepaMandatStatus\"]{.jsonkey tag="SepaMandatStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                 |   Aufzählung, Integer                 1=[Neu]{tag="Neu"}\                 |
|                                                                                 |                                       2=[Aktiv]{tag="Aktiv"}\             |
|                                                                                 |                                       3=[InAktiv]{tag="InAktiv"}\         |
|                                                                                 |                                       4=[Widerrufen]{tag="Widerrufen"}    |
|                                                                                 |                                                                           |
|                                                                                 |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatAddItem .anchor}

::: jsonproto
[SepaMandatAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                  |
|                                                                                                                                    |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                             |
|     [\"MandatReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                             |
|     [\"MandatArt\"]{.jsonkey}: [\...]{.jsonvalue},              [SepaMandatArt](#Parameter_SepaMandatArt){.navlinkcomment}         |
|     [\"MandatTyp\"]{.jsonkey}: [\...]{.jsonvalue},              [SepaMandatTyp](#Parameter_SepaMandatTyp){.navlinkcomment}         |
|     [\"MandatStatus\"]{.jsonkey}: [\...]{.jsonvalue},           [SepaMandatStatus](#Parameter_SepaMandatStatus){.navlinkcomment}   |
|     [\"Einreichfrist\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                            |
|     [\"GueltigAb\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                  |
|     [\"GueltigBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                  |
|     [\"AktiviertBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}      date (yyyy-mm-dd)                                                  |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                    |
| }                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatListItem .anchor}

::: jsonproto
[SepaMandatListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                  |
|                                                                                                                                    |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"SepaMandat_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                             |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                             |
|     [\"MandatReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                             |
|     [\"MandatStatus\"]{.jsonkey}: [\...]{.jsonvalue},           [SepaMandatStatus](#Parameter_SepaMandatStatus){.navlinkcomment}   |
|     [\"MandatArt\"]{.jsonkey}: [\...]{.jsonvalue},              [SepaMandatArt](#Parameter_SepaMandatArt){.navlinkcomment}         |
|     [\"MandatTyp\"]{.jsonkey}: [\...]{.jsonvalue}               [SepaMandatTyp](#Parameter_SepaMandatTyp){.navlinkcomment}         |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                    |
| }                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatItem .anchor}

::: jsonproto
[SepaMandatItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                    |
|                                                                                                                                      |
|   --------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"SepaMandat_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                             |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, readonly                                                   |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                             |
|     [\"MandatReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                             |
|     [\"MandatStatus\"]{.jsonkey}: [\...]{.jsonvalue},             [SepaMandatStatus](#Parameter_SepaMandatStatus){.navlinkcomment}   |
|     [\"MandatArt\"]{.jsonkey}: [\...]{.jsonvalue},                [SepaMandatArt](#Parameter_SepaMandatArt){.navlinkcomment}         |
|     [\"MandatTyp\"]{.jsonkey}: [\...]{.jsonvalue},                [SepaMandatTyp](#Parameter_SepaMandatTyp){.navlinkcomment}         |
|     [\"Einreichfrist\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                            |
|     [\"GueltigAb\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                                  |
|     [\"GueltigBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         date (yyyy-mm-dd)                                                  |
|     [\"AktiviertBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                  |
|     [\"WiderrufenAm\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                  |
|     [\"LetzteVerwendung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   date (yyyy-mm-dd)                                                  |
|     [\"ErstelltAm\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          date (yyyy-mm-dd), readonly                                        |
|   --------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                      |
| }                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SepaMandatPrintItem .anchor}

::: jsonproto
[SepaMandatPrintItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------+
| {                                                                                                   |
|                                                                                                     |
|   --------------------------------------------------------- --------------------------------------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                  |
|     [\"Dateigroesse\"]{.jsonkey}: [ \... ]{.jsonvalue},     integer                                 |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                  |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Raw-Daten in BASE64-Kodierung   |
|   --------------------------------------------------------- --------------------------------------- |
|                                                                                                     |
| }                                                                                                   |
+-----------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BelegAusgabe .anchor}

::: jsonproto
[BelegAusgabe]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
neu ab Version 22.0
:::

+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| { [\"BelegAusgabe\"]{.jsonkey tag="BelegAusgabe"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------- |
|                                                                         |   Aufzählung, Integer                 0=[Ausdruck/PDf]{tag="Ausdruck/PDf"}\   |
|                                                                         |                                       1=[XRechnung]{tag="XRechnung"}\         |
|                                                                         |                                       2=[ZUGFeRD 2.x]{tag="ZUGFeRD 2.x"}      |
|                                                                         |                                                                               |
|                                                                         |   ----------------------------------- --------------------------------------- |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------+
::::

\
[]{#Parameter_ERechnungProfil .anchor}

::: jsonproto
[ERechnungProfil]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
neu ab Version 22.0
:::

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| { [\"ERechnungProfil\"]{.jsonkey tag="ERechnungProfil"}: [\...]{.jsonvalue} } |   ----------------------------------- ---------------------------------------------------- |
|                                                                               |   Aufzählung, Integer                 0=[unbekannt]{tag="unbekannt"}\                      |
|                                                                               |                                       1=[Basic (EN 16931)]{tag="Basic (EN 16931)"}\        |
|                                                                               |                                       2=[Comfort (EN 16931)]{tag="Comfort (EN 16931)"}\    |
|                                                                               |                                       4=[Extended (EN 16931)]{tag="Extended (EN 16931)"}   |
|                                                                               |                                                                                            |
|                                                                               |   ----------------------------------- ---------------------------------------------------- |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
::::

\
[]{#adressen .anchor}\

### Funktionsliste von Adressen

[]{#adressen_adresseFilterTemplate .anchor}

::::: memitem
::: memproto
[adresseFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Adressen-Filter

**Aufruf:**
:   { \"adresseFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"adresseFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                            |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AdresseFilter\": {\...} } ]{.jsonvalue}   [AdresseFilter](#Parameter_AdresseFilter){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |                                                                                                                                              |
    | }                                                                                                                                            |
    +----------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseList .anchor}

::::: memitem
::: memproto
[adresseList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert alle Adressen als Liste

**Aufruf:**
:   { \"adresseList\":
    +-----------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                 |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |     [\"AdresseFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AdresseFilter](#Parameter_AdresseFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |                                                                                                                                   |
    | }                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                        |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AdresseListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [AdresseListItem](#Parameter_AdresseListItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                          |
    | }                                                                                                                                                                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseGet .anchor}

::::: memitem
::: memproto
[adresseGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert Details einer Adresse

**Aufruf:**
:   { \"adresseGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                      |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AdresseItem\": {\...} } ]{.jsonvalue}   [AdresseItem](#Parameter_AdresseItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                                        |
    | }                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAdd .anchor}

::::: memitem
::: memproto
[adresseAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt eine Adresse hinzu

**Aufruf:**
:   { \"adresseAdd\":
    +---------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                         |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |     [\"AdresseAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AdresseAddItem](#Parameter_AdresseAddItem){.navlinkcomment}   |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |                                                                                                                           |
    | }                                                                                                                         |
    +---------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAddResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseModify .anchor}

:::::: memitem
::: memproto
[adresseModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
modifiziert vorhandene Adresse

::: mohelpinfo
\
Ablauf:\
1. Struktur AdresseItem über adresseGet abrufen.Es wird ein gültiger VersionKey geliefert.\
2. Daten von AdresseItem bei Bedarf anpassen.\
3. Funktion adresseModify ausführen.\
Es wird ein Status über Erfolg/Fehler der Operation zurückgeliefert.\
Hinweis: Es sind nicht alle Daten von AdresseItem modifizierbar.\
Es sollten nur die Parameter übergeben werden, welche auch geändert werden sollen. Alle anderen sollten aus AdresseItem entfernt werden.\
\
Beispielaufruf Änderung Vorname (Adresse_ID,VersionKey beispielhaft)\
{\
 \"adresseModify\":{\
    \"AdresseItem\":{\
     \"Adresse_ID\":\"481A62479DF4207DB23598B6461308\",\
     \"VersionKey\":\"99276D86013D6FE47EFB22572D96B63624\",\
     \"RA_Vorname\":\"Paul\"\
   }\
  }\
}
:::

**Aufruf:**
:   { \"adresseModify\":
    +------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                |
    |   ----------------------------------------------------- -------------------------------------------------------- |
    |     [\"AdresseItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AdresseItem](#Parameter_AdresseItem){.navlinkcomment}   |
    |   ----------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                  |
    | }                                                                                                                |
    +------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseModifyResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#adressen_adresseDelete .anchor}

::::: memitem
::: memproto
[adresseDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht vorhandene Adresse

**Aufruf:**
:   { \"adresseDelete\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseDeleteResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseTemplate .anchor}

::::: memitem
::: memproto
[adresseTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert AdresseAddItem als Vorlage

**Aufruf:**
:   { \"adresseTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"adresseTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AdresseAddItem\": {\...} } ]{.jsonvalue}   [AdresseAddItem](#Parameter_AdresseAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseKategorieList .anchor}

::::: memitem
::: memproto
[adresseKategorieList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
ermittelt alle Adress-Kategorien

**Aufruf:**
:   { \"adresseKategorieList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"adresseKategorieListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AdresseKategorieItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [AdresseKategorieItem](#Parameter_AdresseKategorieItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAddAttachment .anchor}

::::: memitem
::: memproto
[adresseAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einer Adresse hinzu

**Aufruf:**
:   { \"adresseAddAttachment\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAddAttachmentResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAnsprechpartnerTemplate .anchor}

::::: memitem
::: memproto
[adresseAnsprechpartnerTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert AnsprechpartnerAddItem als Vorlage

**Aufruf:**
:   { \"adresseAnsprechpartnerTemplate\":
    +--------------------------------------------------------------------------------+
    | {                                                                              |
    |   -------------------------------------------------------- ------------------- |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string (optional)   |
    |   -------------------------------------------------------- ------------------- |
    |                                                                                |
    | }                                                                              |
    +--------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AnsprechpartnerAddItem\": {\...} } ]{.jsonvalue}   [AnsprechpartnerAddItem](#Parameter_AnsprechpartnerAddItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                         |
    | }                                                                                                                                                                       |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAnsprechpartnerList .anchor}

::::: memitem
::: memproto
[adresseAnsprechpartnerList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert alle Ansprechpartner einer Adresse

**Aufruf:**
:   { \"adresseAnsprechpartnerList\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                |
    |   ----------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AnsprechpartnerListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [AnsprechpartnerListItem](#Parameter_AnsprechpartnerListItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                  |
    | }                                                                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAnsprechpartnerAdd .anchor}

::::: memitem
::: memproto
[adresseAnsprechpartnerAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt Ansprechpartner zu Adresse hinzu

**Aufruf:**
:   { \"adresseAnsprechpartnerAdd\":
    +---------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                 |
    |   ---------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"AnsprechpartnerAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AnsprechpartnerAddItem](#Parameter_AnsprechpartnerAddItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                   |
    | }                                                                                                                                                 |
    +---------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerAddResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAnsprechpartnerGet .anchor}

::::: memitem
::: memproto
[adresseAnsprechpartnerGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert Details eines einzelnen Ansprechpartner

**Aufruf:**
:   { \"adresseAnsprechpartnerGet\":
    +-----------------------------------------------------------------------------+
    | {                                                                           |
    |   ---------------------------------------------------------------- -------- |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ---------------------------------------------------------------- -------- |
    |                                                                             |
    | }                                                                           |
    +-----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AnsprechpartnerItem\": {\...} } ]{.jsonvalue}   [AnsprechpartnerItem](#Parameter_AnsprechpartnerItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseAnsprechpartnerModify .anchor}

:::::: memitem
::: memproto
[adresseAnsprechpartnerModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
modifiziert vorhandenen Ansprechpartner

::: mohelpinfo
\
Ablauf:\
1. Struktur AnsprechpartnerItem über adresseAnsprechpartnerGet abrufen.Es wird ein gültiger VersionKey geliefert.\
2. Daten von AnsprechpartnerItem bei Bedarf anpassen.\
3. Funktion adresseAnsprechpartnerModify ausführen.\
Es wird ein Status über Erfolg/Fehler der Operation zurückgeliefert.\
Hinweis: Es sind nicht alle Daten von AnsprechpartnerItem modifizierbar.\
Es sollten nur die Parameter übergeben werden, welche auch geändert werden sollen. Alle anderen sollten aus AnsprechpartnerItem entfernt werden.\
Beispielaufruf Änderung Nachname (Adresse_ID,Ansprechpartner_ID,VersionKey beispielhaft)\
\
{\
 \"adresseAnsprechpartnerModify\":{\
    \"AnsprechpartnerItem\":{\
     \"Adresse_ID\":\"480C644B85E2297DB23598B04C18\",\
     \"Ansprechpartner_ID\":\"4806655E84F42F4A8B10D0F3184C4BC98F057A8BEFAE\",\
     \"VersionKey\":\"067EF8D83D7912D08D53C8CDD06A7E0D73\",\
     \"Nachname\":\"Mustermann\"\
   }\
  }\
}
:::

**Aufruf:**
:   { \"adresseAnsprechpartnerModify\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"AnsprechpartnerItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AnsprechpartnerItem](#Parameter_AnsprechpartnerItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerModifyResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#adressen_adresseAnsprechpartnerDelete .anchor}

::::: memitem
::: memproto
[adresseAnsprechpartnerDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine Ansprechpartner

**Aufruf:**
:   { \"adresseAnsprechpartnerDelete\":
    +-----------------------------------------------------------------------------+
    | {                                                                           |
    |   ---------------------------------------------------------------- -------- |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ---------------------------------------------------------------- -------- |
    |                                                                             |
    | }                                                                           |
    +-----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseAnsprechpartnerDeleteResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatList .anchor}

::::: memitem
::: memproto
[adresseSepaMandatList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung angelegter SEPA-Mandate für Adresse

**Aufruf:**
:   { \"adresseSepaMandatList\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                 |
    |   ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"SepaMandatListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [SepaMandatListItem](#Parameter_SepaMandatListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ |
    |                                                                                                                                                                                   |
    | }                                                                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatTemplate .anchor}

::::: memitem
::: memproto
[adresseSepaMandatTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für neues SEPA-Mandat

**Aufruf:**
:   { \"adresseSepaMandatTemplate\":
    +--------------------------------------------------------------------------------+
    | {                                                                              |
    |   -------------------------------------------------------- ------------------- |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string (optional)   |
    |   -------------------------------------------------------- ------------------- |
    |                                                                                |
    | }                                                                              |
    +--------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                        |
    |   --------------------------------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"SepaMandatAddItem\": {\...} } ]{.jsonvalue}   [SepaMandatAddItem](#Parameter_SepaMandatAddItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                                          |
    | }                                                                                                                                                        |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatAdd .anchor}

::::: memitem
::: memproto
[adresseSepaMandatAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Anlegen eines SEPA-Mandat für Adresse

**Aufruf:**
:   { \"adresseSepaMandatAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"SepaMandatAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [SepaMandatAddItem](#Parameter_SepaMandatAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatAddResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatGet .anchor}

::::: memitem
::: memproto
[adresseSepaMandatGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert Details eines vorhandenen SEPA-Mandat

**Aufruf:**
:   { \"adresseSepaMandatGet\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"SepaMandat_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"SepaMandatItem\": {\...} } ]{.jsonvalue}   [SepaMandatItem](#Parameter_SepaMandatItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatModify .anchor}

::::: memitem
::: memproto
[adresseSepaMandatModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
modifiziert vorhandenes SEPA-Mandat

**Aufruf:**
:   { \"adresseSepaMandatModify\":
    +---------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                         |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |     [\"SepaMandatItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [SepaMandatItem](#Parameter_SepaMandatItem){.navlinkcomment}   |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |                                                                                                                           |
    | }                                                                                                                         |
    +---------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatModifyResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatDelete .anchor}

::::: memitem
::: memproto
[adresseSepaMandatDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht vorhandenes SEPA-Mandat

**Aufruf:**
:   { \"adresseSepaMandatDelete\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"SepaMandat_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatDeleteResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#adressen_adresseSepaMandatPrintPDF .anchor}

::::: memitem
::: memproto
[adresseSepaMandatPrintPDF]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
gibt SEPA-Mandat als PDF aus

**Aufruf:**
:   { \"adresseSepaMandatPrintPDF\":
    +----------------------------------------------------------------------------+
    | {                                                                          |
    |   --------------------------------------------------------------- -------- |
    |     [\"SepaMandat_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string   |
    |     [\"DruckformularName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   --------------------------------------------------------------- -------- |
    |                                                                            |
    | }                                                                          |
    +----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"adresseSepaMandatPrintPDFResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"SepaMandatPrintItem\": {\...} } ]{.jsonvalue}   [SepaMandatPrintItem](#Parameter_SepaMandatPrintItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#Content_artikel .anchor}  \


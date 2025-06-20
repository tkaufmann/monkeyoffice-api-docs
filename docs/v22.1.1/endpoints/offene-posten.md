## Offene Posten

[]{#offenePosten_Datenstrukturen .anchor}

### Datenstrukturen von Offene Posten

[]{#Parameter_OffenePostenArt .anchor}

::: jsonproto
[OffenePostenArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| { [\"OffenePostenArt\"]{.jsonkey tag="OffenePostenArt"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------- |
|                                                                               |   Aufzählung, Integer                 0=[DebitorRechnung]{tag="DebitorRechnung"}\        |
|                                                                               |                                       1=[DebitorGutschrift]{tag="DebitorGutschrift"}\    |
|                                                                               |                                       2=[KreditorRechnung]{tag="KreditorRechnung"}\      |
|                                                                               |                                       3=[KreditorGutschrift]{tag="KreditorGutschrift"}   |
|                                                                               |                                                                                          |
|                                                                               |   ----------------------------------- -------------------------------------------------- |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenListItem .anchor}

::: jsonproto
[OffenePostenListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                            |
|                                                                                                                              |
|   --------------------------------------------------------- ---------------------------------------------------------------- |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                           |
|     [\"Postenart\"]{.jsonkey}: [\...]{.jsonvalue},          [OffenePostenArt](#Parameter_OffenePostenArt){.navlinkcomment}   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                           |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                           |
|     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},            integer                                                          |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                           |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                           |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}         string                                                           |
|   --------------------------------------------------------- ---------------------------------------------------------------- |
|                                                                                                                              |
| }                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenItem .anchor}

::: jsonproto
[OffenePostenItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                       |
|   ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------ |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string                                                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string                                                                                           |
|     [\"Postenart\"]{.jsonkey}: [\...]{.jsonvalue},                                                                   [OffenePostenArt](#Parameter_OffenePostenArt){.navlinkcomment}                                   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 date (yyyy-mm-dd)                                                                                |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                           |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                  string                                                                                           |
|     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                     integer                                                                                          |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                           |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                           |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                           |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                               [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}                                           |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string                                                                                           |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                  string                                                                                           |
|     [\"OffenePostenPositionItemList\"]{.jsonkey}: [ { \"OffenePostenPositionItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [OffenePostenPositionItem](#Parameter_OffenePostenPositionItem){.navlinkcomment}   |
|   ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                       |
| }                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenPositionItem .anchor}

::: jsonproto
[OffenePostenPositionItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+
| {                                                                         |
|                                                                           |
|   ------------------------------------------------------------- --------- |
|     [\"Position\"]{.jsonkey}: [ \... ]{.jsonvalue},             integer   |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string    |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"BetragNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"BetragSteuerFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragSteuerSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"EA_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},             integer   |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}        string    |
|   ------------------------------------------------------------- --------- |
|                                                                           |
| }                                                                         |
+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenAddItem .anchor}

::: jsonproto
[OffenePostenAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                 |
|     [\"Postenart\"]{.jsonkey}: [\...]{.jsonvalue},                                                                      [OffenePostenArt](#Parameter_OffenePostenArt){.navlinkcomment}                                         |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                    string                                                                                                 |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                    date (yyyy-mm-dd)                                                                                      |
|     [\"OffenePostenPositionItemList\"]{.jsonkey}: [ { \"OffenePostenPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [OffenePostenPositionAddItem](#Parameter_OffenePostenPositionAddItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                                |
| }                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenPositionAddItem .anchor}

::: jsonproto
[OffenePostenPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+
| {                                                                         |
|                                                                           |
|   ------------------------------------------------------------- --------- |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string    |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"EA_Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},             integer   |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}        string    |
|   ------------------------------------------------------------- --------- |
|                                                                           |
| }                                                                         |
+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_OffenePostenFilter .anchor}

::: jsonproto
[OffenePostenFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                    |
|                                                                                                                                                      |
|   -------------------------------------------------------- ----------------------------------------------------------------------------------------- |
|     [\"OpDatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     date (yyyy-mm-dd)                                                                         |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                                    |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                                    |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                                    |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                                    |
|     [\"BetragVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                                    |
|     [\"BetragBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                                    |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue}      [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}, -1 steht für alle Zahlungsarten   |
|   -------------------------------------------------------- ----------------------------------------------------------------------------------------- |
|                                                                                                                                                      |
| }                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#offenePosten .anchor}\

### Funktionsliste von Offene Posten

[]{#offenePosten_offenePostenFilterTemplate .anchor}

::::: memitem
::: memproto
[offenePostenFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Offene Posten-Filter

**Aufruf:**
:   { \"offenePostenFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"offenePostenFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"OffenePostenFilter\": {\...} } ]{.jsonvalue}   [OffenePostenFilter](#Parameter_OffenePostenFilter){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#offenePosten_offenePostenListDebitoren .anchor}

::::: memitem
::: memproto
[offenePostenListDebitoren]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung offener Posten Debitoren

**Aufruf:**
:   { \"offenePostenListDebitoren\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |     [\"OffenePostenFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [OffenePostenFilter](#Parameter_OffenePostenFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |                                                                                                                                                  |
    | }                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"offenePostenListDebitorenResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"OffenePostenListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [OffenePostenListItem](#Parameter_OffenePostenListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#offenePosten_offenePostenListKreditoren .anchor}

::::: memitem
::: memproto
[offenePostenListKreditoren]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung offener Posten Kreditoren

**Aufruf:**
:   { \"offenePostenListKreditoren\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |     [\"OffenePostenFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [OffenePostenFilter](#Parameter_OffenePostenFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |                                                                                                                                                  |
    | }                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"offenePostenListKreditorenResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"OffenePostenListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [OffenePostenListItem](#Parameter_OffenePostenListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#offenePosten_offenePostenGet .anchor}

::::: memitem
::: memproto
[offenePostenGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details eines Posten

**Aufruf:**
:   { \"offenePostenGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   ------------------------------------------------------- --------    |
    |     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string      |
    |   ------------------------------------------------------- --------    |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"offenePostenGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"OffenePostenItem\": {\...} } ]{.jsonvalue}   [OffenePostenItem](#Parameter_OffenePostenItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#Content_projekte .anchor}  \


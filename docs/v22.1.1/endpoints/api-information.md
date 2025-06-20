## API Information

[]{#apiinfo_Datenstrukturen .anchor}

### Datenstrukturen von API Information

[]{#Parameter_apiInfoItem .anchor}

::: jsonproto
[apiInfoItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------+
| {                                                                                             |
|                                                                                               |
|   ------------------------------------------------------------------- ----------------------- |
|     [\"App_Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                  |
|     [\"App_Homepage\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                  |
|     [\"App_Email\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                  |
|     [\"App_MajorVersion\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                 |
|     [\"App_MinorVersion\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                 |
|     [\"App_BugVersion\"]{.jsonkey}: [ \... ]{.jsonvalue},             integer                 |
|     [\"App_Build\"]{.jsonkey}: [ \... ]{.jsonvalue},                  integer                 |
|     [\"App_APISchemaVersion\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
|     [\"App_CopyRight\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                  |
|     [\"App_NewVersion\"]{.jsonkey}: [ \... ]{.jsonvalue}              boolean (true\|false)   |
|   ------------------------------------------------------------------- ----------------------- |
|                                                                                               |
| }                                                                                             |
+-----------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_apisessionInfoItem .anchor}

::: jsonproto
[apisessionInfoItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                             |
|                                                                                                                                                                               |
|   ---------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
|     [\"App_Datenbank\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                     string                                                                       |
|     [\"App_DBSchemaVersion\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                               string                                                                       |
|     [\"Firma_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                          string                                                                       |
|     [\"Benutzer_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string                                                                       |
|     [\"User_Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                         string                                                                       |
|     [\"UserAccessItemList\"]{.jsonkey}: [ { \"UserAccessItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [UserAccessItem](#Parameter_UserAccessItem){.navlinkcomment}   |
|   ---------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
|                                                                                                                                                                               |
| }                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_UserAccessItem .anchor}

::: jsonproto
[UserAccessItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------+
| {                                                                                  |
|                                                                                    |
|   -------------------------------------------------------- ----------------------- |
|     [\"Modul_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                  |
|     [\"ModulName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
|     [\"Zugriff\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)   |
|     [\"Anlegen\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)   |
|     [\"Aendern\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)   |
|     [\"Loeschen\"]{.jsonkey}: [ \... ]{.jsonvalue}         boolean (true\|false)   |
|   -------------------------------------------------------- ----------------------- |
|                                                                                    |
| }                                                                                  |
+------------------------------------------------------------------------------------+
:::

\
[]{#apiinfo .anchor}\

### Funktionsliste von API Information

[]{#apiinfo_apiInfoGet .anchor}

::::: memitem
::: memproto
[apiInfoGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Infos zum aktuellenAPI

**Aufruf:**
:   { \"apiInfoGet\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"apiInfoGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                      |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"apiInfoItem\": {\...} } ]{.jsonvalue}   [apiInfoItem](#Parameter_apiInfoItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                                        |
    | }                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#apiinfo_apisessionInfoGet .anchor}

::::: memitem
::: memproto
[apisessionInfoGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Infos zur aktuellen Session

**Aufruf:**
:   { \"apisessionInfoGet\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"apisessionInfoGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"apisessionInfoItem\": {\...} } ]{.jsonvalue}   [apisessionInfoItem](#Parameter_apisessionInfoItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

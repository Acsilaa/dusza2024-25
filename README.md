## A StillNincsenCsapatnév nevű csapat munkája

## Előr elétrehozott felhasználók
### szervezők:
- szervezo1 (jelszó: organiser1)
- szervezo2 (jelszó: organiser2)

### iskolák:
- MechwartIgazgato (jelszó: school1)
- PeldaIgazgato (jelszó: example1)

### versenyzők:
- versenyzo1 (jelszó: contestant1)
- versenyzo2 (jelszó: contestant2)
- versenyzo3 (jelszó: contestant3)

# A webapplikáció használata
A főoldalt az ip címen érjük el.

### Versenyzőként való használat
Bejelentkezni a navigációs sávban lévő "Bejelentkezés" linkre való kattintás után tudunk. Ha nincs fiókunk, akkor a "Regisztráció"-ra kell kattintani.

Regisztrációnál egy beépített Django felhasználót hozunk létre, amely egy alap Role-t kap, ami a versenyzői szerepkör.

Ezután be kell jelentkeznünk. Bejelentkezés után a képernyő, amit kapunk a jelenlegi verseny határidejétől függ. Ha le van zárva a jelentkezés, vagy lejárt a jelentkezési határidő, akkor egy üzenetet kapunk, hogy majd a következő jelentkezési időszakban tudunk csapatot regisztrálni.

Ha lehet csapatot regisztrálni, akkor megkapjuk rá a lehetőséget egy gomb formájában. Ez átirányít minket egy oldalra, ahol regisztrálni tudunk egy csapatot, ami ez után látható lesz a felhasználó számára, miután bejelentkezett. Az ehhez tartozó adatokat a verseny leírásának megfelelően tudja módosítani később.

Ha egy szervező hiánypótlásra küldött ki kérést, akkor a jobb felső sarokból lehet azt elérni.

Kijelentkezni jobb felül a felhasználónév melletti "Kijelentkezés" gombbal lehet.

### Szervezőként való használat
Szervezőt regisztrálni nem lehet biztonsági okokból. A DJangoAdmin felületen tud a superuser létrehozni egy user-t, és ahhoz organiser Group-ot adni.

Bejelentkezés után egy irányítópult fogad minket.\
Lehetőségünk van módosítani a jelentkezési határidőt, vagy akár lezárni a jelentkezéseket.

Emellett (Ajax kérésekkel megoldva) tudunk kategóriákat és programnyelveket kezelni. A beviteli mezőbe írva a kívánt szöveget, majd a hozzáadás gombot megnyomva. Ha törölni akarunk, akkor pedig értelemszerűen a törlés gombot kell használnunk.

Szervezőként lehetőségünk van a regisztrált iskolák megjelenítésére, és akár új iskolák regisztrálására. Ezt a navigációs sávban érjük el az "Iskolák megtekintése" fül alatt.

A jelentkezéseket a navigációs sávból érjük el. Itt lehetőségünk van letölteni egy .csv fájlt, ami tartalmazza az összes csapat adatát. Ha egy csapatot szeretnénk kezelni, a mellette lévő "Több" gombot kell megnyomnunk. Itt látjuk a részletes adatokat, illetve megvan a lehetőség a jóváhagyásra, illetve a pdf letöltésére, amit az igazgató töltött fel, mikor jóváhagyta az iskolájából jelentkező csapat jelentkezését. Ha hiányosnak akarjuk jelenteni a jelentkezést, akkor egy beviteli mezőbe tudjuk írni az üzenetünket, majd elküldhetjük.

### Iskolai kapcsolattartóként való használat
Bejelentkezés után az iskola adataival fogad minket a weblap. Igény esetén ezek módosíthatóak. Alább pedig az iskola neve alatt jelentkezett csapatokat láthatjuk. Mellettük egy gomb, "Jóváhagyás" címmel. Erre kattintva feltölthetünk egy pdf-et, ezzel jóváhagyva a csapat jelentkezését.


# Adatbázis
Szerencsére nem sok táblából áll az adatbázis. Próbáltuk minél tisztábban tartani a munkakörnyezetet. A táblák a következők: Team, Contest, Category, Language, School és a beépített User.
A Category és a Language csak egy-egy name fieldet tartalmaznak, de hasznosak, mikor foreign kulcsokkal hivatkozunk rájuk.

A Team tábla tartalmazza az adatokat a csapatokról, illetve azt, hogy az igazgató és a szervezők által jóvá lettek e hagyva (2 boolean formájában).

A Contest tábla érdekes, mert mindig csak egy record van benne. Ez csak arra kell, hogy legyen hol eltárolni a jelentkezési határidőt, és hogy le lehessen zárni a jelentkezést.

A School tábla tartalmazza az iskolákat és adataikat.
```
├── School
│   ├── user (Foreign Key)
│   ├── name (Char)
│   ├── address (Char)
│   ├── contact_name (Char)
│   └── contact_email (Char)
├── Team
│   ├── user (Foreign Key)
│   ├── name (Char)
│   ├── school (Foreign Key)
│   ├── contestant1_name (Char)
│   ├── contestant1_grade (Decimal)
│   ├── contestant2_name (Char)
│   ├── contestant2_grade (Decimal)
│   ├── contestant3_name (Char)
│   ├── contestant3_grade (Decimal)
│   ├── contestant4_name (Char)
│   ├── contestant4_grade (Decimal)
│   ├── teachers (Text)
│   ├── category (Foreign Key)
│   ├── language (Foreign Key)
│   ├── approved (Boolean)
│   ├── approval_file (Char)
│   ├── missing (Char)
│   ├── joined (Boolean)
│   └── date_modified (Datetime)
├── User
│   ├── password (Char)
│   ├── last_logined (Datetime)
│   ├── is_superuser (Boolean)
│   ├── username (Char)
│   ├── is_staff (Boolean)
│   ├── is_active (Boolean)
│   └── date_joined (Datetime)
├── Contest
│   ├── join_deadline (Datetime)
│   └── joining_closed (Boolean)
├── Category
│   └── name (Char)
├── Language
│   └── name (Char)
└── Groups
    └── name (Char)
```
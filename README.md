# Tech-Corp
# TechCorp HR & Payroll Management System

Sistem i brendshëm në Python për menaxhimin e punonjësve dhe pagave në TechCorp, i ndërtuar si projekt praktik OOP (Programim i Orientuar në Objekte).

## Përmbajtja e Projektit

TechCorp është një kompani teknologjike me rreth 30 punonjës, e cila deri tani i ka menaxhuar të dhënat e stafit me spreadsheet dhe llogaritje manuale. Ky projekt zhvillon një aplikacion Python (CLI – Command Line Interface) që i lehtëson HR-it:

- Menaxhimin e informacionit të punonjësve
- Organizimin e punonjësve sipas departamenteve
- Llogaritjen e pagave dhe bonuseve
- Kërkimin dhe raportimin e të dhënave
- Ruajtjen dhe ngarkimin e informacionit (persistencë e të dhënave)

## Ekipi

| Anëtari | Grupi | Fokusi kryesor |
|---|---|---|
| Ajla Aliu     | Grupi A | Modeli i punonjësve (Employee) |
| Amjona Trpeza | Grupi A | Departamentet (Department) |
| Omer Aliu     | Grupi A | Serializimi (to_dict / from_dict) dhe testimi |
| Suhela Hetemi | Grupi B | Logjika e kompanisë (Company) |
| Elmedin Ilazi | Grupi B | Persistenca e të dhënave dhe main.py |

**Mentor/Profesor:** Qefser Karpuzi — Scantech Academy

## Struktura e Projektit

Tech-Corp/
├── employee.py # Klasa abstrakte Employee + nënklasat (Developer, Manager, Accountant)
├── department.py # Klasa Department – menaxhon listën e punonjësve të një departamenti
├── company.py # Klasa Company – menaxhon të gjitha departamentet e kompanisë
├── main.py # Pika hyrëse e programit – menuja kryesore për HR-in
└── README.md


## Konceptet e OOP të Përdorura

- **Abstraksioni** – `Employee` është klasë abstrakte (`ABC`), me metodën abstrakte `calculate_salary()`
- **Trashëgimia (Inheritance)** – `Developer`, `Manager` dhe `Accountant` trashëgojnë nga `Employee`
- **Polimorfizmi** – çdo nënklasë e implementon `calculate_salary()` ndryshe, sipas rregullave të veta të pagës/bonusit
- **Enkapsulimi** – atributet e brendshme (`__id`, `__name`, `__base_salary`, etj.) janë private dhe aksesohen përmes `@property`

## Funksionalitetet e Deritanishme

- [x] Krijimi i punonjësve të llojeve të ndryshme (Developer, Manager, Accountant)
- [x] Llogaritja e pagës për secilin lloj punonjësi, sipas rregullave specifike
- [x] Organizimi i punonjësve në departamente
- [x] Shtimi i punonjësve në një departament (me kontroll ID-je të dyfishtë)
- [x] Krijimi i kompanisë dhe menaxhimi i shumë departamenteve
- [x] Kërkimi i një punonjësi brenda kompanisë
- [x] Llogaritja e pagës totale mujore të kompanisë (payroll)
- [x] Ruajtja dhe ngarkimi i të dhënave në format JSON
- [x] Menu bazë në terminal për operacionet kryesore

## Si Ekzekutohet

```bash
python main.py
```

Programi hap një menu në terminal ku HR-i mund të zgjedhë opsionin e duhur (shtim, kërkim, shikim, llogaritje pagash, ruajtje/ngarkim, dalje).

## Git Workflow

Projekti zhvillohet drejtpërdrejt në versionin kryesor të kodit, pa përdorur degë (branches) ose Pull Request-e.

## Statusi Aktual

🔧 **Fazë: Zhvillim (Development)** — struktura bazë e sistemit është e ndërtuar dhe funksionon. Ekipi vazhdon me forcimin e validimit, veçori shtesë dhe testim para se të kalohet në fazën e testimit final dhe prezantimit.

## Kërkesat Teknike

- Python 3.x
- Vetëm librari standarde (nuk kërkohen paketa shtesë)
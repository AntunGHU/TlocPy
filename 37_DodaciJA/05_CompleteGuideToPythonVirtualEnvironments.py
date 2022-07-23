# 15'41

# pocinje s objasnjenjem ovisnosti rada projekta u buducnosti obzirom na stalan razvoj komponenti - rjesenje: zamrzavanje stanja kroz venv!
# najjednostavniji alat danas je "venv" - builtin library sa komandom
# ? python3.x -m venv venvName
# Win
# ? python.exe -m venv venvName
# ? python -V

# Aktivacija venv-a
# Win iz cmd
# ? echo %PATH%      # izbacuje gomilu pathova
# ? source venvName/bin/activate     # Lin
# ? source venvName/Scripts/activate     # Win sa git ili bash
# ? venvName\Scripts\activate.bat       # Win sa cmd ili powershell
# ispred prompta se pojavljuje (venvName), ako sad ponovo
# ? echo %PATH%      # izbacuje gomilu pathova ali prvi je path do naseg projekta!!!
# ako ukucamo kdu za veziju pythona
# ? python -V       # Python 3.8.2 (zato sto smo i kreirali venv sa tom verzijom, da smo s drugom bio bi taj drugi)
# sad kad je aktiviran i pip koji run-amo nije onaj glavni nego localni

# Instalacija u venv
# sve sto instaliramo sa localnim pip-om ostaje localno!

# Sta sa venv?
# Trebamo pratiti i voditi racuna o svim dependencijama u projektu. To obicno radimo praveci spisak unutar file-a "requirements.txt" koji je u root-u projekta. Spisak moze biti sa tocim brojevima verzija koje koristimo, npr flask==1.0.0 gdje == kaze installeru da nadje tocno tu verziju!
# Brojevi uz pakete: 1-major ver(incremented whenever major changes are made like architectural changes), 2-minor ver(new features which don't break API), 3-Patch ver(bug fixes) . Promjene 2 i 3 obicno ne lome API pa je njihovo upgrejdanje uobicajeno, ali... To cinimo dajuci slobodu unutar "requirements.txt" tako da napisemonpr flask>=1.1.2,<2.0
# Ako koristimo poneke libse samo tjekom developmenta (testiranja, deployment i sl) ali ne i za rad app-a  tada ih pisemo u fajl "requirements-dev.txt"

# Rekreacija dependencija
# Nakon stvaranja VirtEnva te njegova aktiviranja pokrecemo k-du
# ? pip install -r requirements.txt

# Alternativa venv-u: pipenv

#Computer Application In Civil Engineering

#BOATENG CHRISTIAN
#6932821
#Github Link: https://github.com/droxybellinton/Boateng-Christian.git

#Available cars and their prices
AvailableCars={
    "Bentley Bentayga":300000,
    "Mercedes-Maybach Exelero":8000000,
    "Bugatti Divo":32000000,
    "Pagani LmoLa":6000000,
    "Centodieci Bugatti":9000000,
    "Mercedes GLA":200000,
    "MacLaren Senna":922000,
    "Porsche 918 Spyder":822000,
    "RUF CTR3 Clubsport":652000,
    "Ford GT (Mk II 656 PS)":530000,
    "Ferrari SF90 Stradale":448000,
    "Lamborghini Aventador SVJ":23000000,
    "Devel Sixteen":1000000,
    "Picanto":34000000,
    "Nissan GT":23000000,
    "Chiron":80000000,
    "Aston Martin":2600000,
    "Ferrari Roma":78000000,
    "Audi R8 V10 Performance RWD":1000000000,
    "Mercedes Benz AMG":12000000,
    "Bugatti Veyron":186000000,
    "Murcielago":200000,
    "GT1 Fahlke Larea":700000,
    "Brabus SL 850":420000,
    "Ford GT Sport":345879,
    "Maserati MC20":786900,
    "Land Rover":500700,
    "Range Rover":456000,
    "Toyota Highlander":234000,
    "Matiz":123000,
    "Kantanka Sports":426000,
    "Ferrari 488 GTB":765000,
    "Koenigsegg CC8S":567000,
    "RUF RT12":234000,
    "McLaren 675LT":345000,
    "RUF RT 35 Roadster":145000,
    "Saleen S7 Twin Turbo":6789000,
    "Brabus Maybach":564999,
    "Pagani Zonda":999999,
    "Porsche Carrera GT":567000,
    "Porsche 919 Spyder":345560,
    "Ferrari 489 GTB":8755500,
    "Bentley Continental GT Speed Convertible":5673333,
    "Lamborghini Huracan Tecnica":345567,
    "De Tomaso P72":8007600,
    "Brabus 800 (W213)":8044000,
    "Ferrari LeFerrari":8043350,
    "McLaren Elva":766300,
    "Czinger 21C":1345666,
    "Ferrari Monza":6867454,
    "Gordon Murray":200888,
    "Koenigsegg Gemera":5543000,
    "Zenvo TSR-S":33345000,
    "Hannessey Venom F5":9987700,
    "Bentley Bacalar":1065789900999,
    "Hispano Suiza Carmen Boulogne":3345600,
    "Bentley Mulliner Batur":99988877,
    "Deus Vaynne":135678,
    "SSC Tuatara":13579,
    "Lotus Evija":246810,
    "Delaga D12":56677788,
    "Rimac Nevera":2344566,
    "Pagani Utopia":6778990
    }
car_name=input("Type car_name:")
if car_name in AvailableCars:
    print("Yes, check the price below")
    car_price=AvailableCars[car_name]
    print(f"The price of {car_name} is ${car_price}.")
else:
    print(f"Pease, sorry.{car_name} is not available.")
    
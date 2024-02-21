class Moon:
    fullname = ""
    difficulty = ""
    risk = ""
    cost = 0
    weather = "mild"
    minscrap = 0
    maxscrap = 0

class Item:
    fullname = ""
    price = 0

class Scrap:
    fullname = ""
    minval = 0
    maxval = 0

class Drop:
    fullname = ""
    prev = 0
    curr = 0

class Cell:
    fullname = ""
    stringname = ""
    amount = 0

class Inventory:
    Airhorn = Cell("Airhorn","Airhorn",0)
    Apparatus = Cell("Apparatus","Apparatus",0)
    BeeHive = Cell("Bee Hive","Bee Hive",0)
    BigBolt = Cell("Big bolt","Big bolt",0)
    Bottles = Cell("Bottles","Bottles",0)
    BrassBell = Cell("Brass bell","Brass bell",0)
    Candy = Cell("Candy","Candy",0)
    CashRegister = Cell("Cash register","Cash register",0)
    ChemicalJug = Cell("Chemical jug","Chemical jug",0)
    ClownHorn = Cell("Clown horn","Clown horn",0)
    Mug = Cell("Coffee mug","Coffee mug",0)
    Comedy = Cell("Comedy","Comedy",0)
    Pan = Cell("Cookie mold pan","Cookie mold pan",0)
    DIYFlashbang = Cell("DIY-Flashbang","DIY-Flashbang",0)
    DoubleBarrel = Cell("Double-barrel","Double-barrel",0)
    DustPan = Cell("Dust pan","Dust pan",0)
    EggBeater = Cell("Egg beater","Egg beater",0)
    FancyLamp = Cell("Fancy lamp","Fancy lamp",0)
    Flask = Cell("Flask","Flask",0)
    GiftBox = Cell("Gift Box","Gift Box",0)
    GoldBar = Cell("Gold bar","Gold bar",0)
    GoldCup = Cell("Golden cup","Golden cup",0)
    HairBrush = Cell("Hair brush","Hair brush",0)
    HairDryer = Cell("Hairdryer","Hairdryer",0)
    JarOfPickles = Cell("Jar of pickles","Jar of pickles",0)
    LargeAxle = Cell("Large axle","Large axle",0)
    LaserPointer = Cell("Laser pointer","Laser pointer",0)
    Magic7Ball = Cell("Magic 7 ball","Magic 7 ball",0)
    MagnifyingGlass = Cell("Magnifying glass","Magnifying glass",0)
    OldPhone = Cell("Old phone","Old phone",0)
    Painting = Cell("Painting","Painting",0)
    PerfumeBottle = Cell("Perfume bottle","Perfume bottle",0)
    PillBottle = Cell("Pill bottle","Pill bottle",0)
    PlasticFish = Cell("Plastic fish","Plastic fish",0)
    RedSoda = Cell("Red soda","Red soda",0)
    Remote = Cell("Remote","Remote",0)
    Ring = Cell("Ring","Ring",0)
    RobotToy = Cell("Robot toy","Robot toy",0)
    RubberDucky = Cell("Rubber Ducky","Rubber Ducky",0)
    SteeringWheel = Cell("Steering wheel","Steering wheel",0)
    StopSign = Cell("Stop sign","Stop sign",0)
    TatteredMetalSheet = Cell("Tattered metal sheet","Tattered metal sheet",0)
    TeaKettle = Cell("Tea kettle","Tea kettle",0)
    Teeth = Cell("Teeth","Teeth",0)
    Toothpaste = Cell("Toothpaste","Toothpaste",0)
    ToyCube = Cell("Toy cube","Toy cube",0)
    Tragedy = Cell("Tragedy","Tragedy",0)
    VTypeEngine = Cell("V-type engine","V-type engine",0)
    WhoopieCushion = Cell("Whoopie-Cushion","Whoopie-Cushion",0)
    YieldSign = Cell("Yield sign","Yield sign",0)
    

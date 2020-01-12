import json

json_string = """{
  "Test Data": [
    {
      "№": "1",
      "user_id": "24457",
      "Name": "Dmytrenko Nina",
      "Email": "olenka_j_191@generator.local",
      "Flow": "Just Recruiter"
    },
    {
      "№": "2",
      "user_id": "24456",
      "Name": "Kramarenko Serhii",
      "Email": "olenka_j_115@generator.local",
      "Flow": " 2-2"
    },
    {
      "№": "3",
      "user_id": "24455",
      "Name": "Shevchenko Yevhen",
      "Email": "olenka_j_128@generator.local",
      "Flow": "2-2, 3-1"
    },
    {
      "№": "4",
      "user_id": "24454",
      "Name": "Shevchenko Mykola",
      "Email": "olenka_j_86@generator.local",
      "Flow": "2-2, 3-2"
    },
    {
      "№": "5",
      "user_id": "24453",
      "Name": "Sereda Biktor",
      "Email": "olenka_j_68@generator.local",
      "Flow": "2-2, 3-3"
    },
    {
      "№": "6",
      "user_id": "24452",
      "Name": "Sereda Stanislav",
      "Email": "olenka_j_85@generator.local",
      "Flow": "2-2, 3-2, 4-1"
    },
    {
      "№": "7",
      "user_id": "24451",
      "Name": "Tarashchuk Yevhen",
      "Email": "olenka_j_129@generator.local",
      "Flow": "2-2, 3-2, 4-2"
    },
    {
      "№": "8",
      "user_id": "24450",
      "Name": "Dmytrenko Kira",
      "Email": "olenka_j_101@generator.local",
      "Flow": "2-2, 3-2, 4-3"
    },
    {
      "№": "9",
      "user_id": "24449",
      "Name": "Kravchuk Raisa",
      "Email": "olenka_j_76@generator.local",
      "Flow": "2-2, 3-2, 4-2, 5-1"
    },
    {
      "№": "10",
      "user_id": "24448",
      "Name": "Shevchenko Diana",
      "Email": "olenka_j_116@generator.local",
      "Flow": "2-2, 3-2, 4-2, 5-2"
    },
    {
      "№": "11",
      "user_id": "24447",
      "Name": "Antonenko Artem",
      "Email": "olenka_j_92@generator.local",
      "Flow": "2-2, 3-2, 4-2, 5-3"
    },
    {
      "№": "12"
    },
    {
      "№": "13",
      "user_id": "24446",
      "Name": "Ponomarchuk Raisa",
      "Email": "olenka_j_150@generator.local",
      "Flow": "2-2, 5-1"
    },
    {
      "№": "14",
      "user_id": "24445",
      "Name": "Kravchuk Boleslav",
      "Email": "olenka_j_30@generator.local",
      "Flow": "2-2, 5-2"
    },
    {
      "№": "15",
      "user_id": "24444",
      "Name": "Vasyliev Vira",
      "Email": "olenka_j_50@generator.local",
      "Flow": "2-2, 5-3"
    },
    {
      "№": "16",
      "user_id": "24443",
      "Name": "Mykytiuk Danylo",
      "Email": "olenka_j_87@generator.local",
      "Flow": "2-2, 3-1, 5-1"
    },
    {
      "№": "17",
      "user_id": "24442",
      "Name": "Hnatiuk Kateryna",
      "Email": "olenka_j_3@generator.local",
      "Flow": "2-2, 3-1, 5-2"
    },
    {
      "№": "18",
      "user_id": "24441",
      "Name": "Kravchuk Kira",
      "Email": "olenka_j_149@generator.local",
      "Flow": "2-2, 3-1, 5-3"
    },
    {
      "№": "19",
      "user_id": "24440",
      "Name": "Sereda Valerii",
      "Email": "olenka_j_121@generator.local",
      "Flow": "2-2, 3-2, 5-1"
    },
    {
      "№": "20",
      "user_id": "24439",
      "Name": "Panasiuk Volodymyr",
      "Email": "olenka_j_32@generator.local",
      "Flow": "2-2, 3-2, 5-2"
    },
    {
      "№": "21",
      "user_id": "24438",
      "Name": "Kramarchuk Lev",
      "Email": "olenka_j_39@generator.local",
      "Flow": "2-2, 3-2, 5-3"
    },
    {
      "№": "22",
      "user_id": "24437",
      "Name": "Tarashchuk Biktor",
      "Email": "olenka_j_82@generator.local",
      "Flow": "2-2, 3-2, 4-1, 5-1"
    },
    {
      "№": "23",
      "user_id": "24436",
      "Name": "Bodnarenko Biktor",
      "Email": "olenka_j_171@generator.local",
      "Flow": "2-2, 3-2, 4-1, 5-2"
    },
    {
      "№": "24",
      "user_id": "24435",
      "Name": "Shevchenko Biacheslav",
      "Email": "olenka_j_105@generator.local",
      "Flow": "2-2, 3-2, 4-1, 5-3"
    }
  ]
}"""

parsed_string = json.loads(json_string)
for i in parsed_string['Test Data']:
    if i['№'] == '3':
        name = i['Name']
        print(name)








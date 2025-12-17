import pandas as pd

data = [
["Arjun Mehta",32,"Mumbai","9876543001","Andheri East",150000,400000,720,55000],
["Riya Sharma",28,"Delhi","9876543002","Saket",0,300000,690,48000],
["Kunal Verma",35,"Bengaluru","9876543003","Whitefield",250000,600000,750,70000],
["Sneha Iyer",30,"Chennai","9876543004","T Nagar",100000,350000,680,45000],
["Vikram Rao",40,"Hyderabad","9876543005","Banjara Hills",300000,800000,790,95000],
["Manya Khurana",26,"Pune","9876543006","Koregaon Park",0,250000,710,42000],
["Siddharth Jain",29,"Jaipur","9876543007","Malviya Nagar",120000,500000,705,52000],
["Aditi Nair",31,"Kochi","9876543008","Marine Drive",50000,300000,660,40000],
["Rohit Kulkarni",34,"Nagpur","9876543009","Ramdaspeth",0,450000,735,60000],
["Tanvi Bhat",27,"Bengaluru","9876543010","Indiranagar",200000,550000,745,68000],
["Harsh Patel",33,"Ahmedabad","9876543011","Vastrapur",0,380000,700,50000],
["Shruti Deshmukh",29,"Pune","9876543012","Aundh",90000,300000,695,48000],
["Naveen Reddy",38,"Hyderabad","9876543013","Madhapur",350000,900000,810,100000],
["Priya Sinha",24,"Delhi","9876543014","Hauz Khas",0,200000,705,35000],
["Ankit Malhotra",36,"Mumbai","9876543015","Bandra West",280000,700000,720,75000],
["Divya Garg",28,"Chandigarh","9876543016","Sector 22",0,260000,650,38000],
["Karan Singh",31,"Amritsar","9876543017","Ranjit Avenue",0,300000,710,45000],
["Roshni Pillai",33,"Thiruvananthapuram","9876543018","Kowdiar",130000,400000,690,50000],
["Deepak Chauhan",45,"Delhi","9876543019","Karol Bagh",400000,950000,820,120000],
["Megha Kapoor",27,"Noida","9876543020","Sec 62",0,280000,675,42000],
["Aditya Bhatt",30,"Gurgaon","9876543021","DLF Phase 3",150000,550000,740,68000],
["Nikita Rawat",26,"Dehradun","9876543022","Rajpur Road",0,240000,710,39000],
["Varun Saxena",39,"Indore","9876543023","Vijay Nagar",320000,850000,785,92000],
["Aisha Khan",29,"Mumbai","9876543024","Kurla West",180000,450000,705,56000],
["Gaurav Mishra",34,"Kanpur","9876543025","Swaroop Nagar",0,350000,700,50000],
["Anushka Rao",32,"Hyderabad","9876543026","Gachibowli",140000,500000,720,64000],
["Rahul Nair",41,"Kochi","9876543027","Edapally",380000,950000,830,130000],
["Jyoti Sharma",25,"Jaipur","9876543028","C-Scheme",0,230000,690,35000],
["Shreyas Kulkarni",37,"Pune","9876543029","Baner",260000,600000,760,78000],
["Sara George",33,"Kochi","9876543030","Panampilly Nagar",150000,420000,700,52000],
["Aman Arora",28,"Delhi","9876543031","Lajpat Nagar",0,300000,710,46000],
["Neha Bansal",31,"Gurgaon","9876543032","Sushant Lok",90000,400000,685,48000],
["Yashwant Reddy",43,"Hyderabad","9876543033","Kukatpally",370000,880000,795,110000],
["Kripa Iyer",27,"Chennai","9876543034","Velachery",0,260000,730,45000],
["Jay Mehta",30,"Mumbai","9876543035","Lower Parel",200000,600000,745,70000],
["Shalini Rao",34,"Bengaluru","9876543036","Jayanagar",0,420000,760,62000],
["Abhishek Chauhan",29,"Lucknow","9876543037","Aliganj",70000,350000,700,45000],
["Pooja Chatterjee",32,"Kolkata","9876543038","Park Street",150000,500000,720,58000],
["Manoj Gupta",36,"Bhopal","9876543039","Arera Colony",250000,750000,780,85000],
["Ritika Malhotra",28,"Delhi","9876543040","Janakpuri",0,290000,705,42000],
["Samar Shetty",31,"Mangalore","9876543041","Bejai",120000,400000,690,46000],
["Farhan Siddiqui",35,"Lucknow","9876543042","Gomti Nagar",180000,550000,720,59000],
["Mitali Desai",29,"Surat","9876543043","City Light",0,300000,700,43000],
["Kabir Joshi",33,"Vadodara","9876543044","Alkapuri",160000,450000,705,55000],
["Simran D’Souza",27,"Goa","9876543045","Panaji",0,250000,690,38000],
["Aarav Mahajan",38,"Chandigarh","9876543046","Sec 15",300000,800000,770,93000],
["Lavanya Krishnan",30,"Chennai","9876543047","Adyar",90000,500000,720,65000],
["Keshav Saxena",42,"Indore","9876543048","Old Palasia",350000,900000,815,105000]
]

columns = ["name","age","city","phone","address","existing_loan","preapproved_limit","credit_score","monthly_salary"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("mock_customers.csv", index=False)

print("mock_customers.csv generated successfully!")

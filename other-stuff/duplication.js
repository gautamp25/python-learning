let data = [{
          countyName: "Holy Cross",
          stateId: "Alaska",
          isActive: true,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          countyName: "Holy Cross1",
          stateId: "Alaska",
          isActive: true,
          createdAt: new Date(),
          updatedAt: new Date(),
        }
      ]

  let b = data.map(d=>{
    console.log(d.countyName)
  })
       
  data.forEach((key,index)=>{
    console.log(key[index].countyName)
  })
//   for i in range(str_len-1):
//   if s[i] == s[i+1]:
//       print("1",s[i])
//       print("2",s[i+1])
//       count += 1
//   else:
//       new_str = new_str + s[i] + str(count)
//       count = 1
//   # print(count)
// new_str = new_str + s[str_len-1] + str(count)
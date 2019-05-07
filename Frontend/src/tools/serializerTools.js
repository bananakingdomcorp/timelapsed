//Eventually this will become part of an NPM tooling package. 

//For now, we will just call this as an export. 

export const timeParser = (key, times) => {
  let res = {}
  let split = key.split(' ')
  let day = new Date(key)
  res['Day'] = day.toLocaleDateString('en-US',{weekday: 'long'})
  res['Begin_Date'] = `${split[3]}-${day.getMonth() +1}-${split[2]}`

  times[key].forEach((item) => {
    let time = item[0].split(',')
    res['Begin_Time'] = time[0]
    res['End_Time'] = time[1].trim()
    res['Num_Weeks'] = item[1]
    res['Weeks_Skipped'] = item[2]
  })

  return res;
}
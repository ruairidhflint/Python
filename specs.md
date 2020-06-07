# Website Blocker Spec 

A Python Application that runs behind the scenes blocking access to websites as per a users choosing. 

## MVP Specs
- A list of blocked websites is stored in a .txt file for ease of editing ✓
- Script pulls list of websites and appends them to the blocked list in hosts file ✓
- Script is automatically run via Cron  ✓
- List is responsive and dynamically read eg: if an item is removed from the .txt file, it is removed from
  the blocked list too  ✓

## Second Iteration
- Ability to add times/dates to block websites and allow usage at other times ✓
- Build GUI for Application 

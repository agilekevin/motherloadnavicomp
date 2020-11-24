# Commands

## Overview of command design

### Fluent
Commands should read like a sentence.
Good: `/plotCourse from [sector] to [sector]`
Bad: `/plotCourse [sector] [sector]`

### Respond with Context
Wherever possible, provide "the next question".  Ex: the `/move` command provides the expected arrival time, even though you could get that information by calling /plotCourse


## Notes and Ideas

### Mining material chain
Maybe you have to *use* one material to get another?  Like we use cyanide to get gold?

### Scanner distance
Maybe you can scan adjacent sectors?

### Travel time math
"The further you go, the faster you go."
Something like accelerating at 1g halfway, then decelerating at 1g, if it doesn't make the math too ridiculously difficult.

### loading/processing questions
Some commands could indicate time passing or other systems.  LIke the `/pay` command could print some 'establishing secure connection' type of thing.

## Mining Ship Commands
### Move
`/move to [sector]`:
```
Moving to [sector]. Expected arrival time [dd:hh:mm]
```

### Plot
`/plotCourse from [sector] to [sector]

### Status
`/status`:
```
Current location: [sector]
Moving to [sector], expected arrival time [dd:hh:mm]
Extracting [MineralType] at a rate of [units/hour], [dd:hh:mm] until tanks full
```

### Scan
`/scan [sector]`:
```
Minerals:
[MineralType: volume @ density]
Ships:
[Shipname, shiptags]
```

### Extract
`/extract MineralType`:
```
Extracting [MineralType] at a rate of [units/hour].  Time until full tanks: [dd:hh:mm]
```

Extracts the provided mineralType from the ship's current sector.

Density = mining speed, volume is total amount.

### Transfer
`/transfer [quantity] of [mineralType] to [target]`

### plink
`/plink [targetShip]`
```
Harpoonlinked [targetship]
-or-
[targetship] not in sector
```
If possible, creates a private discord channel between the two players.

## Mothership commands for all

### Pay
`/pay [quantity] credits to [target]`

### Balance
`/balance`
```
Current balance: 283 credits
```

## Mothership commands for corp
How much help do we want to be in tracking the miners' "payments"?  When corp is an NPC, probably none. In fact, these commands could be covered by the scaffolded web app.
### show
`/show balance [miner]`

`/show transactions [miner]`
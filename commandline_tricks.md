sudo nvram SystemAudioVolume=%80

defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false

cal 12 2013

NSMutableDictionary *crew = [NSMutableDictionary dictionaryWithObjectsAndKeys:@"Dave", @"Captain", @"Heywood", @"Scientist", @"Frank", @"Engineer", nil];

[crew setObject:@"Hal" forKey:@"Crazy Computer"];

[crew removeObjectForKey:@"Engineer"];

for (id role in crew) {
  NSLog(@"%@: %@", role, [crew objectForKey:role]);
};
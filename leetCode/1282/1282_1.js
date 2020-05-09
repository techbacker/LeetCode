var groupThePeople = function(groupSizes) {
  const groupMap = groupSizes.reduce((map, curr, i) => {
      map.has(curr) ? map.get(curr).push(i) : map.set(curr, [i]);
      return map;
  }, new Map());
  return [...groupMap.keys()].reduce((res, key) => {
      const arr = [], group = groupMap.get(key);
      while(group.length) {
          arr.push(group.splice(0, key));
      }
      return [...res, ...arr];
  }, []);
};

console.log(groupThePeople([3,3,3,3,3,1,3]))
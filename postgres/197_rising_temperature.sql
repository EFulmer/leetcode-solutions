select w1.id from weather as w1, weather as w2 where w1.recorddate - w2.recorddate = 1 and w1.temperature - w2.temperature > 0;

const sdk = require('api')('@climacell-docs/v4.0.1#w8bjo1ilf6r6prj');

sdk.auth('WgX3pBOikmlLo5MDTzfdHPaYuSqyhuMZ');
sdk.getTimelines({
  location: '42.3478%2C%20-71.0466',
  fields: 'temperature',
  units: 'metric',
  timesteps: '1h',
  startTime: 'now',
  endTime: 'nowPlus6h',
  'accept-encoding': 'gzip'
})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));
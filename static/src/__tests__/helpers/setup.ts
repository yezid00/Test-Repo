import enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

enzyme.configure({ adapter: new Adapter() });

// This monkey patches document.createEvent so that MouseEvents have a `pageX` value.
// This is intended to prevent React from adding window listeners when a component is mounted using enzyme.
const originalCreateEvent = document.createEvent;

document.createEvent = function(type: string): any {
  const event = originalCreateEvent.call(this, type);

  if (type === 'MouseEvent') {
    event.pageX = 0;
  }

  return event;
};

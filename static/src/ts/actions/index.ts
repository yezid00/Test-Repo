import { ActionNoPayload } from './types';

export const INCREMENT = 'INCREMENT';
export const increment = (): ActionNoPayload => ({
  type: INCREMENT,
});

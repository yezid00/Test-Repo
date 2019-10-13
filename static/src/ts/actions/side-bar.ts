import { ActionNoPayload } from './types';

export const OPEN_SIDE_BAR = 'OPEN_SIDE_BAR';
export const openSideBar = (): ActionNoPayload => ({
  type: OPEN_SIDE_BAR,
});

export const CLOSE_SIDE_BAR = 'CLOSE_SIDE_BAR';
export const closeSideBar = (): ActionNoPayload => ({
  type: CLOSE_SIDE_BAR,
});

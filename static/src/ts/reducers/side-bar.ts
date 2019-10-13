import { AnyAction } from 'redux';

import * as sideBarActions from '^/actions/side-bar';

export const sideBarOpen = (state: boolean = false, action: AnyAction) => {
  switch (action.type) {
    case sideBarActions.OPEN_SIDE_BAR:
      return true;
    case sideBarActions.CLOSE_SIDE_BAR:
      return false;
    default:
      return state;
  }
};

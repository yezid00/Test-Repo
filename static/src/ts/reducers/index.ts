import { combineReducers } from 'redux';

import * as actions from '^/actions';
import { Action } from '^/actions/types';
import { StoreState } from '^/store/types';
import * as sideBarReducers from './side-bar';

function count(state = 0, action: Action<any, any>) {
  switch (action.type) {
    case actions.INCREMENT:
      return state + 1;
    default:
      return state;
  }
}

export default combineReducers<StoreState>({
  ...sideBarReducers,
  count,
});

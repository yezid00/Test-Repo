import { ThunkAction } from 'redux-thunk';

export interface Action<Payload, Meta> {
  type: string;
  payload?: Payload;
  error?: boolean;
  meta?: Meta;
}

export type ActionNoPayload = Action<undefined, undefined>;

export type ThunkActionOrAction =
  | Action<any, any>
  | ThunkAction<any, any, undefined, any>;

// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: stock/stock.proto

package stock

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/golang/protobuf/ptypes"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = ptypes.DynamicAny{}
)

// Validate checks the field values on Account with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *Account) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Code

	// no validation rules for Balance

	// no validation rules for AvgByPrice

	// no validation rules for TotalPrice

	return nil
}

// AccountValidationError is the validation error returned by Account.Validate
// if the designated constraints aren't met.
type AccountValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountValidationError) ErrorName() string { return "AccountValidationError" }

// Error satisfies the builtin error interface
func (e AccountValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccount.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountValidationError{}

// Validate checks the field values on AccountRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *AccountRequest) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Account

	return nil
}

// AccountRequestValidationError is the validation error returned by
// AccountRequest.Validate if the designated constraints aren't met.
type AccountRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountRequestValidationError) ErrorName() string { return "AccountRequestValidationError" }

// Error satisfies the builtin error interface
func (e AccountRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccountRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountRequestValidationError{}

// Validate checks the field values on AccountReply with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *AccountReply) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Info

	return nil
}

// AccountReplyValidationError is the validation error returned by
// AccountReply.Validate if the designated constraints aren't met.
type AccountReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountReplyValidationError) ErrorName() string { return "AccountReplyValidationError" }

// Error satisfies the builtin error interface
func (e AccountReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccountReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountReplyValidationError{}

// Validate checks the field values on TickRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *TickRequest) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Codes

	return nil
}

// TickRequestValidationError is the validation error returned by
// TickRequest.Validate if the designated constraints aren't met.
type TickRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e TickRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e TickRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e TickRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e TickRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e TickRequestValidationError) ErrorName() string { return "TickRequestValidationError" }

// Error satisfies the builtin error interface
func (e TickRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sTickRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = TickRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = TickRequestValidationError{}

// Validate checks the field values on TickReply with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *TickReply) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Price

	if v, ok := interface{}(m.GetDate()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TickReplyValidationError{
				field:  "Date",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	// no validation rules for Volume

	return nil
}

// TickReplyValidationError is the validation error returned by
// TickReply.Validate if the designated constraints aren't met.
type TickReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e TickReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e TickReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e TickReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e TickReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e TickReplyValidationError) ErrorName() string { return "TickReplyValidationError" }

// Error satisfies the builtin error interface
func (e TickReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sTickReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = TickReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = TickReplyValidationError{}

// Validate checks the field values on ChartRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *ChartRequest) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Code

	if v, ok := interface{}(m.GetTo()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return ChartRequestValidationError{
				field:  "To",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// ChartRequestValidationError is the validation error returned by
// ChartRequest.Validate if the designated constraints aren't met.
type ChartRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ChartRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ChartRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ChartRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ChartRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ChartRequestValidationError) ErrorName() string { return "ChartRequestValidationError" }

// Error satisfies the builtin error interface
func (e ChartRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sChartRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ChartRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ChartRequestValidationError{}

// Validate checks the field values on ChartReply with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *ChartReply) Validate() error {
	if m == nil {
		return nil
	}

	for idx, item := range m.GetData() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return ChartReplyValidationError{
					field:  fmt.Sprintf("Data[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// ChartReplyValidationError is the validation error returned by
// ChartReply.Validate if the designated constraints aren't met.
type ChartReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ChartReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ChartReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ChartReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ChartReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ChartReplyValidationError) ErrorName() string { return "ChartReplyValidationError" }

// Error satisfies the builtin error interface
func (e ChartReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sChartReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ChartReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ChartReplyValidationError{}

// Validate checks the field values on AccountsReply with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *AccountsReply) Validate() error {
	if m == nil {
		return nil
	}

	for idx, item := range m.GetAccounts() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return AccountsReplyValidationError{
					field:  fmt.Sprintf("Accounts[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// AccountsReplyValidationError is the validation error returned by
// AccountsReply.Validate if the designated constraints aren't met.
type AccountsReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountsReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountsReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountsReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountsReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountsReplyValidationError) ErrorName() string { return "AccountsReplyValidationError" }

// Error satisfies the builtin error interface
func (e AccountsReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccountsReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountsReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountsReplyValidationError{}

// Validate checks the field values on BuyRequest with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *BuyRequest) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Code

	// no validation rules for Otype

	// no validation rules for Volume

	// no validation rules for Price

	return nil
}

// BuyRequestValidationError is the validation error returned by
// BuyRequest.Validate if the designated constraints aren't met.
type BuyRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e BuyRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e BuyRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e BuyRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e BuyRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e BuyRequestValidationError) ErrorName() string { return "BuyRequestValidationError" }

// Error satisfies the builtin error interface
func (e BuyRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sBuyRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = BuyRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = BuyRequestValidationError{}

// Validate checks the field values on BuyReply with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *BuyReply) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Id

	// no validation rules for Code

	// no validation rules for AvgPrice

	// no validation rules for Volume

	// no validation rules for Fee

	// no validation rules for Price

	if v, ok := interface{}(m.GetCreatedAt()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return BuyReplyValidationError{
				field:  "CreatedAt",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// BuyReplyValidationError is the validation error returned by
// BuyReply.Validate if the designated constraints aren't met.
type BuyReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e BuyReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e BuyReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e BuyReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e BuyReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e BuyReplyValidationError) ErrorName() string { return "BuyReplyValidationError" }

// Error satisfies the builtin error interface
func (e BuyReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sBuyReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = BuyReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = BuyReplyValidationError{}

// Validate checks the field values on SellRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *SellRequest) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// SellRequestValidationError is the validation error returned by
// SellRequest.Validate if the designated constraints aren't met.
type SellRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SellRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SellRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SellRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SellRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SellRequestValidationError) ErrorName() string { return "SellRequestValidationError" }

// Error satisfies the builtin error interface
func (e SellRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSellRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SellRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SellRequestValidationError{}

// Validate checks the field values on SellReply with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *SellReply) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// SellReplyValidationError is the validation error returned by
// SellReply.Validate if the designated constraints aren't met.
type SellReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SellReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SellReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SellReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SellReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SellReplyValidationError) ErrorName() string { return "SellReplyValidationError" }

// Error satisfies the builtin error interface
func (e SellReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSellReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SellReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SellReplyValidationError{}

// Validate checks the field values on ChartData with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *ChartData) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Open

	// no validation rules for High

	// no validation rules for Low

	// no validation rules for Close

	// no validation rules for Volume

	if v, ok := interface{}(m.GetDate()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return ChartDataValidationError{
				field:  "Date",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// ChartDataValidationError is the validation error returned by
// ChartData.Validate if the designated constraints aren't met.
type ChartDataValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ChartDataValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ChartDataValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ChartDataValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ChartDataValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ChartDataValidationError) ErrorName() string { return "ChartDataValidationError" }

// Error satisfies the builtin error interface
func (e ChartDataValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sChartData.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ChartDataValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ChartDataValidationError{}

// Validate checks the field values on OrderListRequest with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *OrderListRequest) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// OrderListRequestValidationError is the validation error returned by
// OrderListRequest.Validate if the designated constraints aren't met.
type OrderListRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e OrderListRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e OrderListRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e OrderListRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e OrderListRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e OrderListRequestValidationError) ErrorName() string { return "OrderListRequestValidationError" }

// Error satisfies the builtin error interface
func (e OrderListRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sOrderListRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = OrderListRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = OrderListRequestValidationError{}

// Validate checks the field values on OrderListReply with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *OrderListReply) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// OrderListReplyValidationError is the validation error returned by
// OrderListReply.Validate if the designated constraints aren't met.
type OrderListReplyValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e OrderListReplyValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e OrderListReplyValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e OrderListReplyValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e OrderListReplyValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e OrderListReplyValidationError) ErrorName() string { return "OrderListReplyValidationError" }

// Error satisfies the builtin error interface
func (e OrderListReplyValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sOrderListReply.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = OrderListReplyValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = OrderListReplyValidationError{}

// Validate checks the field values on CancelOrderRequest with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *CancelOrderRequest) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Id

	return nil
}

// CancelOrderRequestValidationError is the validation error returned by
// CancelOrderRequest.Validate if the designated constraints aren't met.
type CancelOrderRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e CancelOrderRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e CancelOrderRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e CancelOrderRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e CancelOrderRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e CancelOrderRequestValidationError) ErrorName() string {
	return "CancelOrderRequestValidationError"
}

// Error satisfies the builtin error interface
func (e CancelOrderRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sCancelOrderRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = CancelOrderRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = CancelOrderRequestValidationError{}
